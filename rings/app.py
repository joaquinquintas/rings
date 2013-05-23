import tornado.web

from rings.social import home

def setup_app(settings):
    # intialize our tornado instance
    routes = []
    routes.extend(home.routes)
    
    app = tornado.web.Application(routes, **settings)
    return app
