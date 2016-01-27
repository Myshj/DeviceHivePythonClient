from Permission import Permission

class AccessKey(object):

    def __init__(self, id=None, type=None, label=None, key=None, expirationDate=None, permissions=[]):

        self.id = id

        self.type = type

        self.label = label

        self.key = key

        self.expirationDate = expirationDate

        self.permissions = permissions

    def ToDictionary(self):
        return {"id": self.id,
                "type": self.type,
                "label": self.label,
                "key": self.key,
                "expirationDate": self.expirationDate,
                "permissions": [permission.ToDictionary() for permission in self.permissions] if self.permissions else []}

    @staticmethod
    def FromDictionary(dict):

        return AccessKey(dict["id"] if "id" in dict.keys() else None,
                         dict["type"] if "type" in dict.keys() else 0,
                         dict["label"] if "label" in dict.keys() else None,
                         dict["key"] if "key" in dict.keys() else None,
                         dict["expirationDate"] if "expirationDate" in dict.keys() else None,
                         [Permission.FromDictionary(permissionDict) for permissionDict in dict["permissions"]] if "permissions" in dict.keys() and dict["permissions"] else [])