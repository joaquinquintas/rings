# coding=utf-8

import tornado
from tornado.web import RequestHandler
from rings.utils.json_parser import JSONParser
from rings.utils.app_ctx import AppCTX

#STATUS_SUCCESS = "success"
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
