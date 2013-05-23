# coding=utf-8

import json
import sys

import tornado.httpserver
import tornado.ioloop

from rings.app import setup_app
from rings.utils.app_ctx import AppCTX
from rings.utils.settings_loader import SettingsLoader

def start_instance(settings):

    app_ctx = AppCTX.get_instance()
    app_ctx.settings = settings
    app_ctx.logger = settings["LOGGER"]

    http_server = tornado.httpserver.HTTPServer(
        setup_app(settings["TORNADO"])
        )
    http_server.listen(settings["TORNADO"]["port"])

    display_server_info(settings)

    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        pass

    print "started"


def display_server_info(settings):
    print ""
    print "===== SERVER INFO ====="
    print ""
    print "Server: Rings (Tornado)"
    print "Environment: %s" % settings["ENVIRONMENT"]
    print "Port: %s" % settings["TORNADO"]["port"]
    print "DB_SETTINGS: %s" % json.dumps(settings["DB_SETTINGS"], indent=2)
    print ""
    print "======================="
    print ""


def display_help():
    print "Use: {environment=prod, qa, dev, local} runserver {port}"



if __name__ == "__main__":
    env = str(sys.argv[1])
    cmd = str(sys.argv[2])
    port = str(sys.argv[3])
    settings = SettingsLoader().load_settings(env)
    settings["TORNADO"]["port"] = port

    if cmd == "runserver":
        start_instance(settings)

    elif cmd == "help":
        display_help()

    else:
        print "Unknown command '%s'" % cmd
        display_help()
