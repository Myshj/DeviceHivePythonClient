class UserCreatedResponse(object):

    def __init__(self, id=None, lastLogin=None, facebookLogin=None, googleLogin=None, githubLogin=None):

        self.id = id

        self.lastLogin = lastLogin

        self.facebookLogin = facebookLogin

        self.googleLogin = googleLogin

        self.githubLogin = githubLogin

    def ToDictionary(self):

        return {"id": self.id,
                "lastLogin": self.lastLogin,
                "facebookLogin": self.facebookLogin,
                "googleLogin": self.googleLogin,
                "githubLogin": self.githubLogin}

    @staticmethod
    def FromDictionary(dict):

        return UserCreatedResponse(id = dict["id"] if "id" in dict.keys() else None,
                                   lastLogin = dict["lastLogin"] if "lastLogin" in dict.keys() else None,
                                   facebookLogin = dict["facebookLogin"] if "facebookLogin" in dict.keys() else None,
                                   googleLogin = dict["googleLogin"] if "googleLogin" in dict.keys() else None,
                                   githubLogin = dict["githubLogin"] if "githubLogin" in dict.keys() else None)