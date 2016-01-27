class OAuthClientCreatedResponse(object):

    def __init__(self, id=None, oauthSecret=None):

        self.id = id

        self.oauthSecret = oauthSecret

    def ToDictionary(self):

        return {"id": self.id,
                "oauthSecret": self.oauthSecret}

    @staticmethod
    def FromDictionary(dict):

        return OAuthClientCreatedResponse(id = dict["id"] if "id" in dict.keys() else None,
                                          oauthSecret = dict["oauthSecret"] if "oauthSecret" in dict.keys() else None)