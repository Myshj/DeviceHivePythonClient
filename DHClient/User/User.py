from ..Network import NetworkFull
class User(object):

    def __init__(self, id=None, login=None, facebookLogin=None, googleLogin=None, githubLogin=None,
                 role=None, status=None, lastLogin=None, networks=None):

        self.id = id

        self.login = login

        self.facebookLogin = facebookLogin

        self.googleLogin = googleLogin

        self.githubLogin = githubLogin

        self.role = role

        self.status = status

        self.lastLogin = lastLogin

        self.networks = networks

    def ToDictionary(self):

        return {"id": self.id,
                "login": self.login,
                "facebookLogin": self.facebookLogin,
                "googleLogin": self.googleLogin,
                "githubLogin": self.githubLogin,
                "role": self.role,
                "status": self.status,
                "lastLogin": self.lastLogin,
                "networks": [network.ToDictionary() for network in self.networks]}

    @staticmethod
    def FromDictionary(dict):

        return User(id = dict["id"] if "id" in dict.keys() else None,
                    login = dict["login"] if "login" in dict.keys() else None,
                    facebookLogin = dict["facebookLogin"] if "facebookLogin" in dict.keys() else None,
                    googleLogin = dict["googleLogin"] if "googleLogin" in dict.keys() else None,
                    githubLogin = dict["githubLogin"] if "githubLogin" in dict.keys() else None,
                    role = dict["role"] if "role" in dict.keys() else None,
                    status = dict["status"] if "status" in dict.keys() else None,
                    lastLogin = dict["lastLogin"] if "lastLogin" in dict.keys() else None,
                    networks = [NetworkFull.NetworkFull.FromDictionary(networkDict) for networkDict in dict["networks"]] if "networks" in dict.keys() else [])