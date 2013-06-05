# coding=utf-8

from os import path
import datetime
import logging

#===================================
#   LOGGING
#===================================

LOGGER = logging.getLogger('rings')
hdlr = logging.FileHandler(path.join(path.dirname(__file__), "logs/rings.log"))
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
LOGGER.addHandler(hdlr)
LOGGER.setLevel(logging.INFO)

#===================================
#   TORNADO
#===================================

TORNADO = dict(
    port=6488,
    db_name="",
    db_uri="",
    db_user="",
    db_pass="",
    login_url="/auth/login",
    static_path=path.join(path.dirname(__file__), "static"),
    template_path=path.join(path.dirname(__file__), "templates"),
    cookie_secret="SOMETHING HERE",
    debug=False,
    debug_pdb=False,
)

DB_SETTINGS = {

}

FACEBOOK_APP_ID = "496581487058041"
FACEBOOK_APP_SECRET = "ec46efe8fb2c382ccfee26b6c6ee5d20"

MOVES_CLIENT_ID = "vyph3myalMFdUp70cBMuPHjyC2NSPjy0"
MOVES_CLIENT_SECRET = "HsBMHBYRMD7eYiEUuAX9_K23mW80xnkP9wJyQ4N1o4MyN44pzJfEYKd8351207eZ"

