# coding=utf-8
from rings.social.base_handler import BaseHandler
from rings.utils.route import Route

@Route('/')
class IndexHandler(BaseHandler):

    def get(self):
        self.render("index.html")


routes = Route.get_routes()