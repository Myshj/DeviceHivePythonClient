class DeviceNotification(object):

    def __init__(self, id=None, timestamp=None, notification=None, parameters=None):

        self.id = id

        self.timestamp = timestamp

        self.notification = notification

        self.parameters = parameters

    def ToDictionary(self):

        return {"id": self.id,
                "timestamp": self.timestamp,
                "notification": self.notification,
                "parameters": self.parameters}

    @staticmethod
    def FromDictionary(dict):

        return DeviceNotification(id = dict["id"] if "id" in dict.keys() else None,
                                  timestamp = dict["timestamp"] if "timestamp" in dict.keys() else None,
                                  notification = dict["notification"] if "notification" in dict.keys() else None,
                                  parameters = dict["parameters"] if "parameters" in dict.keys() else None)