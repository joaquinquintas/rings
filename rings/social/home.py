# coding=utf-8

from rings.social.base_handler import BaseHandler
from rings.utils.route import Route
import requests


@Route('/')
class IndexHandler(BaseHandler):

    def get(self):
        user = self.get_current_user()
        if not user:
            self.render("login.html")
        else:
            self.render("home.html", current_user=user)

@Route('/moves/auth/')
class HomeHandler(BaseHandler):

    def get(self):
        code = self.get_argument('code', None)
        user = self.get_current_user()

        if not code:
            error = self.get_argument("error", "")
            self.db.errors.save({"error": error})
        else:
            user["moves_code"] = code
            self.db.user.save(user)
        
        moves_user = requests.get(settings.MOVES_URL%("user/profile", code)).json()
        user["moves_id"] = moves_user["userId"]
        user["moves_first_date"] = moves_user["profile"]["firstDate"]
        self.db.user.save(user)
        
        summary_url = "user/summary/daily/%s" %user["moves_first_date"][:6]
        moves_summary = requests.get(settings.MOVES_URL%(moves_summary, code)).json()
        self.render("home.html", current_user=user, moves_summary=moves_summary)
        

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