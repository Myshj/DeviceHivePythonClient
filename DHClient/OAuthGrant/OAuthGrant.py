from ..AccessKey import AccessKey

from ..OAuthClient import OAuthClient

class OAuthGrant(object):

    def __init__(self, id=None, timestamp=None, authCode=None, client=None, accessKey=None, type=None, accessType=None,
                 redirectUri=None, scope=None, networkIds=[]):
        self.id = id

        self.timestamp = timestamp

        self.authCode = authCode

        self.client = client

        self.accessKey = accessKey

        self.type = type

        self.accessType = accessType

        self.redirectUri = redirectUri

        self.scope = scope

        self.networkIds = networkIds

    def ToDictionary(self):

        return {"id": self.id,
                "timestamp": self.timestamp,
                "authCode": self.authCode,
                "client": self.client.ToDictionary(),
                "accessKey": self.accessKey.ToDictionary(),
                "type": self.type,
                "accessType": self.accessType,
                "redirectUri": self.redirectUri,
                "scope": self.scope,
                "networkIds": self.networkIds}

    @staticmethod
    def FromDictionary(dict):

        return OAuthGrant(id = dict["id"] if "id" in dict.keys() else None,
                          timestamp = dict["timestamp"] if "timestamp" in dict.keys() else None,
                          authCode = dict["authCode"] if "authCode" in dict.keys() else None,
                          client = OAuthClient.OAuthClient.FromDictionary(dict["client"]) if "client" in dict.keys() else None,
                          accessKey = AccessKey.AccessKey.FromDictionary(dict["accessKey"]) if "accessKey" in dict.keys() else None,
                          type = dict["type"] if "type" in dict.keys() else None,
                          accessType = dict["accessType"] if "accessType" in dict.keys() else None,
                          redirectUri = dict["redirectUri"] if "redirectUri" in dict.keys() else None,
                          scope = dict["scope"] if "scope" in dict.keys() else None,
                          networkIds = dict["networkIds"] if "networkIds" in dict.keys() else [])