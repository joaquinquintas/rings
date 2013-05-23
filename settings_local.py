# coding=utf-8

#===================================
#  LOCAL DEV ENVIRONMENT SETTINGS
#===================================
#Tornado run on local developer machine (localhost)

from settings import *


# The following will be used for any DB that does not EXPLICITLY override these values.
DB_SETTINGS_DEFAULT = {
    "host": "localhost",
    "port": 27017,
}
