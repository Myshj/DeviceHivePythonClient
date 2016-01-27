class DeviceCommand(object):

    def __init__(self, id=None, timestamp=None, userId=None, command=None, parameters=None, lifetime=None, status=None, result=None):

        self.id = id

        self.timestamp = timestamp

        self.userId = userId

        self.command = command

        self.parameters = parameters

        self.lifetime = lifetime

        self.status = status

        self.result = result

    def ToDictionary(self):

        return {"id": self.id,
                "timestamp": self.timestamp,
                "userId": self.userId,
                "command": self.command,
                "parameters": self.parameters,
                "lifetime": self.lifetime,
                "status": self.status,
                "result": self.result}

    @staticmethod
    def FromDictionary(dict):

        return DeviceCommand(id = dict["id"] if "id" in dict.keys() else None,
                             timestamp = dict["timestamp"] if "timestamp" in dict.keys() else None,
                             userId = dict["userId"] if "userId" in dict.keys() else None,
                             command = dict["command"] if "command" in dict.keys() else None,
                             parameters = dict["parameters"] if "parameters" in dict.keys() else None,
                             lifetime = dict["lifetime"] if "lifetime" in dict.keys() else None,
                             status = dict["status"] if "status" in dict.keys() else None,
                             result = dict["result"] if "result" in dict.keys() else None)