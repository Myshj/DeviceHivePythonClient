class NetworkLite(object):

    def __init__(self, id=None, key=None, name=None, description=None):

        self.id = id

        self.key = key

        self.name = name

        self.description = description

    def ToDictionary(self):

        return {"id": self.id,
                "key": self.key,
                "name": self.name,
                "description": self.description}

    @staticmethod
    def FromDictionary(dict):

        return NetworkLite(id = dict["id"] if "id" in dict.keys() else None,
                           key = dict["key"] if "key" in dict.keys() else None,
                           name = dict["name"] if "name" in dict.keys() else None,
                           description = dict["description"] if "description" in dict.keys() else None )