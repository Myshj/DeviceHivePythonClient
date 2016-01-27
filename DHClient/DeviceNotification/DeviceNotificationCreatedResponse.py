class DeviceNotificationCreatedResponse(object):

    def __init__(self, id=None, timestamp=None):

        self.id = id

        self.timestamp = timestamp

    def ToDictionary(self):

        return {"id": self.id,
                "timestamp": self.timestamp}

    @staticmethod
    def FromDictionary(dict):

        return DeviceNotificationCreatedResponse(id = dict["id"] if "id" in dict.keys() else None,
                                                 timestamp = dict["timestamp"] if "timestamp" in dict.keys() else None)