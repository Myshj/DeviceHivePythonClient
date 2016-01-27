class Equipment(object):

    def __init__(self, id=None, name=None, code=None, type=None, data=None):

        self.id = id

        self.name = name

        self.code = code

        self.type = type

        self.data = data

    def ToDictionary(self):

        return {"id": self.id,
                "name": self.name,
                "code": self.code,
                "type": self.type,
                "data": self.data}

    @staticmethod
    def FromDictionary(dict):

        return Equipment(id = dict["id"] if "id" in dict.keys() else None,
                         name = dict["name"] if "name" in dict.keys() else None,
                         code = dict["code"] if "code" in dict.keys() else None,
                         type = dict["type"] if "type" in dict.keys() else None,
                         data = dict["data"] if "data" in dict.keys() else None)