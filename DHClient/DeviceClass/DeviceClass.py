from Equipment import Equipment

class DeviceClass(object):

    def __init__(self, id=None, name=None, version=None, isPermanent=None, offlineTimeout=None, data=None, equipment=[]):

        self.id = id

        self.name = name

        self.version = version

        self.isPermanent = isPermanent

        self.offlineTimeout = offlineTimeout

        self.data = data

        self.equipment = equipment

    def ToDictionary(self):

        return {"id": self.id,
                "name": self.name,
                "version": self.version,
                "isPermanent": self.isPermanent,
                "offlineTimeout": self.offlineTimeout,
                "data": self.data,
                "equipment": [equipmentObj.ToDictionary() for equipmentObj in self.equipment] if self.equipment else []}

    @staticmethod
    def FromDictionary(dict):

        return DeviceClass(id = dict["id"] if "id" in dict.keys() else None,
                           name = dict["name"] if "name" in dict.keys() else None,
                           version = dict["version"] if "version" in dict.keys() else None,
                           isPermanent = dict["isPermanent"] if "isPermanent" in dict.keys() else None,
                           offlineTimeout = dict["offlineTimeout"] if "offlineTimeout" in dict.keys() else None,
                           data = dict["data"] if "data" in dict.keys() else None,
                           equipment = [Equipment.FromDictionary(equipmentDict) for equipmentDict in dict["equipment"]] if "equipment" in dict.keys() else [])