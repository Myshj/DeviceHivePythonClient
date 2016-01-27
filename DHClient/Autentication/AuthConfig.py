from Provider import Provider

class AuthConfig(object):

    def __init__(self, providers=[], sessionTimeout=0):

        self.providers = providers

        self.sessionTimeout = sessionTimeout

    def ToDictionary(self):

        return {"providers": self.providers,
                "sessionTimeout": self.sessionTimeout}

    @staticmethod
    def FromDictionary(dict):

        return AuthConfig([Provider.FromDictionary(providerDict) for providerDict in dict["providers"]] if "providers" in dict.keys() and dict["providers"] else [],
                          dict["sessionTimeout"] if "sessionTimeout" in dict.keys() else 0)