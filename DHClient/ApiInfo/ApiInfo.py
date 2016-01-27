

class ApiInfo(object):

    def __init__(self, apiVersion="", serverTimestamp="", webSocketServerUrl=""):

        self.apiVersion = apiVersion

        self.serverTimestamp = serverTimestamp

        self.webSocketServerUrl = webSocketServerUrl

    def ToDictionary(self):
        return {"apiVersion": self.apiVersion,
                "serverTimestamp": self.serverTimestamp,
                "webSocketServerUrl": self.webSocketServerUrl}

    @staticmethod
    def FromDictionary(dict):
        return ApiInfo(dict["apiVersion"], dict["serverTimestamp"], dict["webSocketServerUrl"])