# coding=utf-8

import tornado
import facebook
from pymongo.connection import Connection

from tornado.web import RequestHandler
from rings.utils.json_parser import JSONParser
from rings.utils.app_ctx import AppCTX
from settings import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET
 
STATUS_SUCCESS = "OK"
STATUS_ERROR = "error"


class BaseHandler(RequestHandler):

    _logger = None

    def initialize(self):
        super(BaseHandler, self).initialize()
        #RequestHandler.initialize(self)
        #TODO get this dependecies injected
        app_ctx = AppCTX.get_instance()
        self._logger = app_ctx.logger


    def get_params(self):
        arguments = self.request.arguments
        params = {}
        for key in arguments:
            params[key] = arguments[key][0]

        return params

    def get_str_params(self):
        arguments = self.request.arguments
        params = {}
        for key in arguments:
            params[key] = str(arguments[key][0])

        return params
    
    def get_current_user(self):
            cookies = dict((n, self.cookies[n].value) for n in self.cookies.keys())
            cookie = facebook.get_user_from_cookie(
                cookies, FACEBOOK_APP_ID, FACEBOOK_APP_SECRET)
            if not cookie:
                return None
            user = self.db.users.find_one({"id":cookie["uid"]})
            if not user:
                # TODO: Make this fetch async rather than blocking
                graph = facebook.GraphAPI(cookie["access_token"])
                profile = graph.get_object("me")
                user = {}
                user["id"] = profile["id"]
                user["name"] = profile["name"]
                user["link"] = profile["link"]
                user["access_token"] = cookie["access_token"]
                self.db.users.save(user)
                user = self.db.users.find_one({"id":profile["id"]})
            elif user["access_token"] != cookie["access_token"]:
                user["access_token"] = cookie["access_token"]
                self.db.users.save(user)
                
            return user

    @property
    def db(self):
            if not hasattr(BaseHandler, "_db"):
                BaseHandler._db = Connection().mystats
                
            return BaseHandler._db
    
    def success(self, response=None, status_code=200, user_message=None, dev_message=None):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        if user_message is not None:
            self.set_header("X-User-Message", user_message)
        if dev_message is not None:
            self.set_header("X-Dev-Message", dev_message)
        self.write(JSONParser.to_json(response))

    def error(self, error="", user_message=None, dev_message=None, status_code=500):
        self._logger.error(error)

        if user_message is not None:
            self.set_header("X-User-Message", user_message)
        if dev_message is not None:
            self.set_header("X-Dev-Message", dev_message)
        self.set_status(status_code)
        self.finish()
