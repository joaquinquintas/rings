# coding=utf-8
from rings.social.base_handler import BaseHandler
from rings.utils.route import Route
import requests


@Route('/')
class IndexHandler(BaseHandler):

    def get(self):
        self.render("login.html")

@Route('/home/')
class HomeHandler(BaseHandler):

    def get(self):
        category_url = "http://api.feedzilla.com/v1/categories.json"
        r = requests.get(category_url)
            
        self.render("index.html", categories=r.json())


@Route('/(?P<category>[-\w]+)/(?P<category_id>[-\w]+)')
@Route('/(?P<category>[-\w]+)/(?P<category_id>[-\w]+)/')
class CategoryHandler(BaseHandler):

    def get(self, category, category_id):
        
        url_art = "http://api.feedzilla.com/v1/categories/%s/articles.json" %category_id
        url_subcate = "http://api.feedzilla.com/v1/categories/%s/subcategories.json"%category_id
        category_url = "http://api.feedzilla.com/v1/categories.json"
        
        r = requests.get(category_url)
        articles = requests.get(url_art)
        subcategories = requests.get(url_subcate)
        
        self.render("index.html", articles=articles.json(), subcategories = subcategories.json(), categories=r.json())

routes = Route.get_routes()