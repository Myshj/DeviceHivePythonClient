class Provider(object):

    def __init__(self, name=None, clientId=None):

        self.name = name

        self.clientId = clientId

    def ToDictionary(self):

        return {"name": self.name,
                "clientId": self.clientId}

    @staticmethod
    def FromDictionary(dict):

        return Provider(dict["name"] if "name" in dict.keys() else None,
                        dict["clientId"] if "clientId" in dict.keys() else None)