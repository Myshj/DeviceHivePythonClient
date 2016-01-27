class AccessKeyCreatedResponse(object):

    def __init__(self, id=None, key=None):

        self.id = id

        self.key = key

    def ToDictionary(self):

        return {"id": self.id,
                "key": self.key}

    @staticmethod
    def FromDictionary(dict):

        return AccessKeyCreatedResponse(id = dict["id"] if "id" in dict.keys() else None,
                                        key = dict["key"] if "key" in dict.keys() else None)