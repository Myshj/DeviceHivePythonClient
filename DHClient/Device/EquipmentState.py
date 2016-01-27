class EquipmentState(object):

    def __init__(self, id=None, timestamp=None, parameters=None):

        self.id = id

        self.timestamp = timestamp

        self.parameters = parameters

    def ToDictionary(self):

        return {"id": self.id,
                "timestamp": self.timestamp,
                "parameters": self.parameters}

    @staticmethod
    def FromDictionary(dict):

        return EquipmentState(id=dict["id"] if "id" in dict.keys() else None,
                              timestamp=dict["timestamp"] if "timestamp" in dict.keys() else None,
                              parameters=dict["parameters"] if "parameters" in dict.keys() else None)