# coding=utf-8

#===================================
#   PROD ENVIRONMENT SETTINGS
#===================================
#Tornado run on API2

from settings import *


# The following will be used for any DB that does not EXPLICITLY override these values.
DB_SETTINGS_DEFAULT = {
    "host": "db1",
    "port": 27017,
}
