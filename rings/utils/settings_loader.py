# coding=utf-8


class SettingsLoader():

    def load_settings(self, environment):
        """
        Returns: Dict<String, Object>
        """

        try:
            settings_module = __import__("settings_{}".format(environment))
            settings_map = {}

            for setting_key in dir(settings_module):
                if setting_key == setting_key.upper():
                    settings_map[setting_key] = getattr(settings_module, setting_key)

            for db in settings_map["DB_SETTINGS"].values():
                if "host" not in db:
                    db["host"] = settings_map["DB_SETTINGS_DEFAULT"]["host"]
                if "port" not in db:
                    db["port"] = settings_map["DB_SETTINGS_DEFAULT"]["port"]

            settings_map["ENVIRONMENT"] = environment

            # If the project uses tornado, run in debug mode.
            if "TORNADO" in settings_map:
                settings_map["TORNADO"]["ENVIRONMENT"] = environment
                settings_map["TORNADO"]['debug'] = environment in ['local', 'dev']

            return settings_map
        except ImportError as e:
            raise ImportError("Could not import settings '{}' (Is it on sys.path? Does it have syntax errors?):\n{}".format((environment, e)))
