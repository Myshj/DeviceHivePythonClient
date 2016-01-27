from ..AccessKey import AccessKey

class OAuthGrantCreatedResponse(object):

    def __init__(self, id=None, timestamp=None, authCode=None, accessKey=None):

        self.id = id

        self.timestamp = timestamp

        self.authCode = authCode

        self.accessKey = accessKey

    def ToDictionary(self):

        return {"id": self.id,
                "timestamp": self.timestamp,
                "authCode": self.authCode,
                "accessKey": self.accessKey.ToDictionary()}

    @staticmethod
    def FromDictionary(dict):

        return OAuthGrantCreatedResponse(id = dict["id"] if "id" in dict.keys() else None,
                                         timestamp = dict["timestamp"] if "timestamp" in dict.keys() else None,
                                         authCode = dict["authCode"] if "authCode" in dict.keys() else None,
                                         accessKey = AccessKey.AccessKey.FromDictionary(dict["accessKey"]) if "accessKey" in dict.keys() else None)
