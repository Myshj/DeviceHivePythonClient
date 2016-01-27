class Device(object):

    def __init__(self, id=None, key=None, status=None, data=None, network=None, deviceClass=None):

        self.id = id

        self.key = key

        self.status = status

        self.data = data

        self.network = network

        self.deviceClass = deviceClass

    def ToDictionary(self):

        return {"id": self.id,
                "key": self.key,
                "status": self.status,
                "data": self.data,
                "network": self.network.ToDictionary(),
                "deviceClass": self.deviceClass.ToDictionary()}

    @staticmethod
    def FromDictionary(dict):

        return Device(id = dict["id"] if "id" in dict.keys() else None,
                      key = dict["key"] if "key" in dict.keys() else None,
                      status = dict["status"] if "status" in dict.keys() else None,
                      data = dict["data"] if "data" in dict.keys() else None,
                      network = dict["network"] if "network" in dict.keys() else None,
                      deviceClass = dict["deviceClass"] if "deviceClass" in dict.keys() else None)