class DeviceCommandCreatedResponse(object):

    def __init__(self, id=None, timestamp=None, userId=None):

        self.id = id

        self.timestamp = timestamp

        self.userId = userId

    def ToDictionary(self):

        return {"id": self.id,
                "timestamp": self.timestamp,
                "userId": self.userId}

    @staticmethod
    def FromDictionary(dict):

        return DeviceCommandCreatedResponse(id = dict["id"] if "id" in dict.keys() else None,
                                            timestamp = dict["timestamp"] if "timestamp" in dict.keys() else None,
                                            userId = dict["userId"] if "userId" in dict.keys() else None)
