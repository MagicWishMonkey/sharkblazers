import util


class Configurator(object):
    def __init__(self, path):
        settings_path = util.io.path_concat(path, "../settings.json")
        settings_override_path = util.io.path_concat(path, "../settings.override.json")
        if util.io.exists(settings_path) is False:
            raise Exception("The settings file could not be found!")

        settings_object = util.io.read_file(settings_path, text=True, fn=util.unjson)
        settings_object = util.wrap(**(settings_object))
        if util.io.exists(settings_override_path):
            override_object = util.io.read_file(settings_override_path, text=True, fn=util.unjson)
            override_object = util.wrap(**(override_object))
            settings_object.override(override_object)

        self.__config__ = settings_object
        self.workspace = path
        self.debug = settings_object.DEBUG
        self.secret_key = settings_object.SECRET_KEY
        self.config = settings_object.reduce()

    def contains(self, param):
        try:
            value = self.config[param]
            return True if value is not None else False
        except:
            return False

    def get(self, param, default=None):
        value = None
        try:
            value = self.config[param]
        except:
            return default

        if value is None:
            return default

        if isinstance(value, list) is True:
            if len(value) > 0 and isinstance(value[0], list) is True:
                value[0] = tuple(value[0])
            value = tuple(value)
        return value


        # def bind(self):
        #     attributes = self.config.keys()
        #     for attribute in attributes:
        #         value = self.config[attribute]
        #         if isinstance(value, list) is True:
        #             if len(value) > 0 and isinstance(value[0], list) is True:
        #                 value[0] = tuple(value[0])
        #             value = tuple(value)
        #
        #         setattr(settings, attribute, value)
        #
        # @classmethod
        # def load(cls, path):
        #     return cls(path)

        # @staticmethod
        # def load(path):
        #     settings_path = __os__.path.normpath(__os__.path.join(path, "../settings.json"))
        #     override_path = __os__.path.normpath(__os__.path.join(path, "../settings.override.json"))
        #     if not __os__.path.exists(settings_path):
        #         raise Exception("The settings file could not be found!")
        #
        #
        #     with __codecs__.open(settings_path, "r", "utf-8") as f:
        #         data = f.read()
        #         config = __json__.loads(data)
        #         config = __Wrapper__.create(**(config))
        #
        #         if __os__.path.exists(override_path):
        #             with __codecs__.open(override_path, "r", "utf-8") as f:
        #                 override_data = f.read()
        #                 override = __json__.loads(override_data)
        #                 override = __Wrapper__.create(**(override))
        #                 config.override(override)
        #
        #     config.PROJECT_PATH = path
        #     config.STATICFILES_DIRS = [__os__.path.join(path, 'static')]
        #     config.TEMPLATE_DIRS = [__os__.path.join(path, 'templates')]
        #
        #
        #     config = config.reduce()
        #     print __util__.json(config, indent=2)
        #     attributes = config.keys()
        #     for attribute in attributes:
        #         value = config[attribute]
        #         if isinstance(value, list) is True:
        #             if len(value) > 0 and isinstance(value[0], list) is True:
        #                 value[0] = tuple(value[0])
        #             value = tuple(value)
        #
        #         setattr(settings, attribute, value)
