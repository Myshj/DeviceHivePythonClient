from ..Device import Device

class NetworkFull(object):

    def __init__(self, id=None, key=None, name=None, description=None, devices=[]):

        self.id = id

        self.key = key

        self.name = name

        self.description = description

        self.devices = devices

    def ToDictionary(self):
        return {"id": self.id,
                "key": self.key,
                "name": self.name,
                "description": self.description,
                "devices": [device.ToDictionary() for device in self.devices]}

    @staticmethod
    def FromDictionary(dict):

        return NetworkFull(id = dict["id"] if "id" in dict.keys() else None,
                           key = dict["key"] if "key" in dict.keys() else None,
                           name = dict["name"] if "name" in dict.keys() else None,
                           description = dict["description"] if "description" in dict.keys() else None,
                           devices = [Device.Device.FromDictionary(deviceDict) for deviceDict in dict["devices"]] if "devices" in dict.keys() else [])