class Permission(object):

    def __init__(self, domains=None, subnets=None, actions=None, networkIds=None, deviceGuids=None):

        self.domains = domains

        self.subnets = subnets

        self.actions = actions

        self.networkIds = networkIds

        self.deviceGuids = deviceGuids

    def ToDictionary(self):

        return {"domains": self.domains,
                "subnets": self.subnets,
                "actions": self.actions,
                "networkIds": self.networkIds,
                "deviceGuids": self.deviceGuids}

    @staticmethod
    def FromDictionary(dictionary):

        return Permission(dictionary["domains"],
                          dictionary["subnets"],
                          dictionary["actions"],
                          dictionary["networkIds"],
                          dictionary["deviceGuids"])