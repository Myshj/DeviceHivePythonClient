class OAuthClient(object):

    def __init__(self, id=None, name=None, domain=None, subnet=None, redirectUri=None, oauthId=None, oauthSecret=None):

        self.id = id

        self.name = name

        self.domain = domain

        self.subnet = subnet

        self.redirectUri = redirectUri

        self.oauthId = oauthId

        self.oauthSecret = oauthSecret

    def ToDictionary(self):

        return {"id": self.id,
                "name": self.name,
                "domain": self.domain,
                "subnet": self.subnet,
                "redirectUri": self.redirectUri,
                "oauthId": self.oauthId,
                "oauthSecret": self.oauthSecret}

    @staticmethod
    def FromDictionary(dict):

        return OAuthClient(id = dict["id"] if "id" in dict.keys() else None,
                           name = dict["name"] if "name" in dict.keys() else None,
                           domain = dict["domain"] if "domain" in dict.keys() else None,
                           subnet = dict["subnet"] if "subnet" in dict.keys() else None,
                           redirectUri = dict["redirectUri"] if "redirectUri" in dict.keys() else None,
                           oauthId = dict["oauthId"] if "oauthId" in dict.keys() else None,
                           oauthSecret = dict["oauthSecret"] if "oauthSecret" in dict.keys() else None)