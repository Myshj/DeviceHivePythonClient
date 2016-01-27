from ThirdParty import requests

from ApiInfo import ApiInfo

from AccessKey import AccessKey

from AccessKey import AccessKeyCreatedResponse

from Autentication import AuthConfig

from DeviceClass import DeviceClass

from Device import Device

from Device import EquipmentState

from Network import NetworkLite

from Network import NetworkFull

from OAuthClient import OAuthClient

from OAuthClient import OAuthClientCreatedResponse

from OAuthGrant import OAuthGrant

from OAuthGrant import OAuthGrantCreatedResponse

from User import User

from User import UserShort

from User import UserCreatedResponse

from DeviceCommand import DeviceCommand

from DeviceCommand import DeviceCommandCreatedResponse

from DeviceNotification import DeviceNotification

from DeviceNotification import DeviceNotificationCreatedResponse

import json

class DHClient(object):

    def __init__(self, url, login, password):
        self.url = url

        self.login = login

        self.password = password

    def GetApiInfo(self):
        """
        Gets meta-information of the current API.
        :return: ApiInfo object.
        """

        r = None

        try:
            r = requests.get(self.url + "/info")
        except:
            return None

        if r.status_code == 200:
            return ApiInfo.ApiInfo.FromDictionary(json.loads(r.text))

        return None

    def ListAccessKeys(self,
                       userId,
                       label=None,
                       labelPattern=None,
                       type=None,
                       sortField=None,
                       sortOrder=None,
                       take=None,
                       skip=None):
        """
        Gets list of access keys and their permissions.
        :param userId: User identifier. Use the 'current' keyword to list access keys of the current user.
        :param label: Filter by access key label.
        :param labelPattern: Filter by access key label pattern.
        :param type: Filter by acess key type.
        :param sortField: Result list sort field. Available values are ID and Label.
        :param sortOrder: Result list sort order. Available values are ASC and DESC.
        :param take: Number of records to take from the result list.
        :param skip: Number of records to skip from the result list.
        :return: List of AccessKey objects.
        """

        jsonToSend = {}

        if label:
            jsonToSend["label"] = label

        if labelPattern:
            jsonToSend["labelPattern"] = labelPattern

        if type:
            jsonToSend["type"] = type

        if sortField:
            jsonToSend["sortField"] = sortField

        if sortOrder:
            jsonToSend["sortOrder"] = sortOrder

        if take:
            jsonToSend["take"] = take

        if skip:
            jsonToSend["skip"] = skip

        r = None

        try:
            r = requests.get(url=self.url+"/user/"+str(userId)+"/accesskey",
                             json=jsonToSend,
                             auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 200:

            return [AccessKey.AccessKey.FromDictionary(accessKeyDict) for accessKeyDict in json.loads(r.text)]

        return None

    def GetAccessKey(self, userId, id):
        """
        Gets information about access key and its permissions.
        :param userId: User identifier. Use the 'current' keyword to get access key of the current user.
        :param id: Access key identifier.
        :return: AccessKey object.
        """

        r = None

        try:
            r = requests.get(url=self.url+"/user/"+str(userId)+"/accesskey/"+str(id),
                             auth=(self.login, self.password))

        except:
            return None

        if r.status_code == 200:

            return AccessKey.AccessKey.FromDictionary(json.loads(r.text))

        return None

    def InsertAccessKey(self, userId, label, type=None, expirationDate=None, permissions=None):
        """
        Creates new access key.
        :param userId: User identifier. Use the 'current' keyword to create access key for the current user.
        :param label: Access key label.
        :param type: Access key type. Available values:
        0: Default
        1: Session (with sliding expiration)
        2: OAuth (issued via OAuth2 token endpoint)
        :param expirationDate: Expiration date (UTC).
        :param permissions: A collection of associated permission objects.
        :return: AccessKeyCreatedResponse object.
        """

        jsonToSend = {"label": label}

        if type:
            jsonToSend["type"] = type

        if expirationDate:
            jsonToSend["expirationDate"] = expirationDate

        if permissions:
            jsonToSend["permissions"] = [permission.ToDictionary() for permission in permissions]

        r = None

        try:
            r = requests.post(url=self.url+"/user/"+str(userId)+"/accesskey",
                              json=jsonToSend,
                              auth=(self.login, self.password))

        except:
            return None

        if r.status_code == 201:

            return AccessKeyCreatedResponse.AccessKeyCreatedResponse.FromDictionary(json.loads(r.text))

        return None

    def UpdateAccessKey(self, userId, id, type=None, label=None, expirationDate=None, permissions=None):
        """
        Updates an existing access key.
        :param userId: User identifier. Use the 'current' keyword to update access key of the current user.
        :param id: Access key identifier.
        :param type: Access key type. Available values:
        0: Default
        1: Session (with sliding expiration)
        2: OAuth (issued via OAuth2 token endpoint)
        :param label: Access key label.
        :param expirationDate: Expiration date (UTC).
        :param permissions: A collection of associated permission objects.
        :return: None
        """
        jsonToSend = {}

        if type:
            jsonToSend["type"] = type

        if label:
            jsonToSend["label"] = label

        if expirationDate:
            jsonToSend["expirationDate"] = expirationDate

        if permissions:
            jsonToSend["permissions"] = [permission.ToDictionary() for permission in permissions]

        try:
            requests.put(url=self.url+"/user/"+str(userId)+"/accesskey/"+str(id),
                         json=jsonToSend,
                         auth=(self.login, self.password))
        except:
            pass

    def DeleteAccessKey(self, userId, id):
        """
        Deletes an existing access key.
        :param userId: User identifier. Use the 'current' keyword to delete access key of the current user.
        :param id: Access key identifier.
        :return: None
        """
        try:
            requests.delete(url=self.url+"/user/"+str(userId)+"/accesskey/"+str(id),
                            auth=(self.login, self.password))
        except:
            pass

    def GetAuthConfig(self):

        """
        Gets information about supported authentication providers.
        :return: List of Provider objects.
        """

        r = None

        try:
            r = requests.get(url=self.url+"/info/config/auth")
        except:
            return None

        if r.status_code == 200:
            return AuthConfig.AuthConfig.FromDictionary(json.loads(r.text))

        return None

    def Login(self, providerName, login=None, password=None, code=None, redirect_uri=None, access_token=None):
        """
        Authenticates a user and returns a session-level access key.
        :param providerName: Name of authentication provider to use. Please call the 'config' method to get the list of available authentication providers. Use the 'password' value for the password-based authentication.
        :param login: When using password authentication, specifies user login.
        :param password: When using password authentication, specifies user password.
        :param code: When using OAuth authentication, specifies authorization code received from provider.
        :param redirect_uri: When using OAuth authentication, specifies redirect uri used during authentication.
        :param access_token: When using OAuth implicit authentication, specifies access code issued to the DeviceHive application.
        :return: AccessKeyCreatedResponse object.
        """
        jsonToSend = {"providerName": providerName}

        if login:
            jsonToSend["login"] = login

        if password:
            jsonToSend["password"] = password

        if code:
            jsonToSend["code"] = code

        if redirect_uri:
            jsonToSend["redirect_uri"] = redirect_uri

        if access_token:
            jsonToSend["access_token"] = access_token

        r = None

        try:
            r = requests.post(url=self.url+"/auth/accesskey",
                              json=jsonToSend)
        except:
            return None

        if r.status_code == 200:
            return AccessKeyCreatedResponse.AccessKeyCreatedResponse.FromDictionary(json.loads(r.text))

        return None

    def Logout(self):
        """
        Invalidates the session-level token.
        :return: None
        """
        try:
            requests.delete(url=self.url+"/auth/accesskey",
                            auth=(self.login, self.password))
        except:
            pass

    def ListDeviceClasses(self, name=None, namePattern=None, version=None, sortField=None, sortOrder=None, take=None, skip=None):
        """
        Gets list of device classes.
        :param name: Filter by device class name.
        :param namePattern: Filter by device class name pattern.
        :param version: Filter by device class version.
        :param sortField: Result list sort field. Available values are ID and Name.
        :param sortOrder: Result list sort order. Available values are ASC and DESC.
        :param take: Number of records to take from the result list.
        :param skip: Number of records to skip from the result list.
        :return: List of DeviceClass objects.
        """
        jsonToSend = {}

        if name:
            jsonToSend["name"] = name

        if namePattern:
            jsonToSend["namePattern"] = namePattern

        if version:
            jsonToSend["version"] = version

        if sortField:
            jsonToSend["sortField"] = sortField

        if sortOrder:
            jsonToSend["sortOrder"] = sortOrder

        if take:
            jsonToSend["take"] = take

        if skip:
            jsonToSend["skip"] = skip

        r = None

        try:
            r = requests.get(url=self.url + "/device/class",
                             json=jsonToSend,
                             auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 200:
            return [DeviceClass.DeviceClass.FromDictionary(deviceClassDict) for deviceClassDict in json.loads(r.text)]

        return None

    def GetDeviceClass(self, id):
        """
        Gets information about device class and its equipment.
        :param id: Device class identifier.
        :return: DeviceClass object.
        """
        r = None

        try:
            r = requests.get(url=self.url + "/device/class/"+str(id),
                             auth=(self.login, self.password))

        except:
            return None

        if r.status_code == 200:
            return DeviceClass.DeviceClass.FromDictionary(json.loads(r.text))

        return None

    def InsertDeviceClass(self, name, version, isPermanent=None, offlineTimeout=None, data=None, equipment=None):
        """
        Creates new device class.
        :param name: Device class display name.
        :param version: Device class version.
        :param isPermanent: Indicates whether device class is permanent. Permanent device classes could not be modified by devices during registration.
        :param offlineTimeout: If set, specifies inactivity timeout in seconds before the framework changes device status to 'Offline'. Device considered inactive when it's not persistently connected and does not send any notifications.
        :param data: Device class data, a JSON object with an arbitrary structure.
        :param equipment: A collection of associated equipment objects.
        :return: Id of created device class.
        """
        jsonToSend = {"name": name,
                      "version": version}

        if isPermanent:
            jsonToSend["isPermanent"] = isPermanent

        if offlineTimeout:
            jsonToSend["offlineTimeout"] = offlineTimeout

        if data:
            jsonToSend["data"] = data

        if equipment:
            jsonToSend["equipment"] = equipment.ToDictionary()

        r = None

        try:
            r = requests.post(url=self.url+"/device/class",
                              json=jsonToSend,
                              auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 201:
            return self.GetDeviceClass(json.loads(r.text)["id"])

        return None

    def UpdateDeviceClass(self, id, name=None, version=None, isPermanent=None, offlineTimeout=None, data=None, equipment=None):
        """
        Updates an existing device class.
        :param id: Device class identifier.
        :param name: Device class display name.
        :param version: Device class version.
        :param isPermanent: Indicates whether device class is permanent. Permanent device classes could not be modified by devices during registration.
        :param offlineTimeout: If set, specifies inactivity timeout in seconds before the framework changes device status to 'Offline'. Device considered inactive when it's not persistently connected and does not send any notifications.
        :param data: If set, specifies inactivity timeout in seconds before the framework changes device status to 'Offline'. Device considered inactive when it's not persistently connected and does not send any notifications.
        :param equipment: A collection of associated equipment objects.
        :return: None.
        """
        jsonToSend = {}

        if name:
            jsonToSend["name"] = name

        if version:
            jsonToSend["version"] = version

        if isPermanent:
            jsonToSend["isPermanent"] = isPermanent

        if offlineTimeout:
            jsonToSend["offlineTimeout"] = offlineTimeout

        if data:
            jsonToSend["data"] = data

        if equipment:
            jsonToSend["equipment"] = equipment.ToDictionary()

        try:
            requests.put(url=self.url+"/device/class/"+str(id),
                         json=jsonToSend,
                         auth=(self.login, self.password))
        except:
            pass

    def DeleteDeviceClass(self, id):
        """
        Deletes an existing device class.
        :param id: Device class identifier.
        :return: None.
        """
        try:
            requests.delete(url=self.url+"/device/class/"+str(id),
                            auth=(self.login, self.password))
        except:
            pass

    def ListDevices(self, name=None, namePattern=None, status=None, networkId=None, networkName=None,
                    deviceClassId=None, deviceClassName=None, deviceClassVersion=None, sortField=None,
                    sortOrder=None, take=None, skip=None):
        """
        Gets list of devices.
        :param name: Filter by device name.
        :param namePattern: Filter by device name pattern.
        :param status: Filter by device status.
        :param networkId: Filter by associated network identifier.
        :param networkName: Filter by associated network name.
        :param deviceClassId: Filter by associated device class identifier.
        :param deviceClassName: Filter by associated device class name.
        :param deviceClassVersion: Filter by associated device class version.
        :param sortField: Result list sort field. Available values are Name, Status, Network and DeviceClass.
        :param sortOrder: Result list sort order. Available values are ASC and DESC.
        :param take: Number of records to take from the result list.
        :param skip: Number of records to skip from the result list.
        :return: List of Device objects.
        """

        jsonToSend = {}

        if name:
            jsonToSend["name"] = name


        if namePattern:
            jsonToSend["namePattern"] = namePattern

        if status:
            jsonToSend["status"] = status

        if networkId:
            jsonToSend["networkId"] = networkId

        if networkName:
            jsonToSend["networkName"] = networkName

        if deviceClassId:
            jsonToSend["deviceClassId"] = deviceClassId

        if deviceClassName:
            jsonToSend["deviceClassName"] = deviceClassName

        if deviceClassVersion:
            jsonToSend["deviceClassVersion"] = deviceClassVersion

        if sortField:
            jsonToSend["sortField"] = sortField

        if sortOrder:
            jsonToSend["sortOrder"] = sortOrder

        if take:
            jsonToSend["take"] = take

        if skip:
            jsonToSend["skip"] = skip

        r = None

        try:
            r = requests.get(url=self.url+"/device",
                             json=jsonToSend,
                             auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 200:
            return [Device.Device.FromDictionary(deviceDict) for deviceDict in json.loads(r.text)]

        return None

    def GetDevice(self, id):
        """
        Gets information about device.
        :param id: Device unique identifier.
        :return: Device object.
        """

        r = None

        try:
            r = requests.get(url=self.url+"/device/"+str(id),
                             auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 200:
            return Device.Device.FromDictionary(json.loads(r.text))

        return None

    def RegisterDevice(self, id, name, deviceClass, key=None, status=None, data=None, network=None):
        """
        Registers or updates a device. For initial device registration, only 'name' and 'deviceClass' properties are required.
        :param id: Device unique identifier.
        :param name: Device display name.
        :param deviceClass: A DeviceClass object which includes name and version properties to match.
        :param key: Device authentication key. The key is set during device registration and it has to be provided for all subsequent calls initiated by device. The key maximum length is 64 characters.
        :param status: Device operation status. The status is optional and it can be set to an arbitrary value, if applicable.
        If device status monitoring feature is enabled, the framework will set status value to 'Offline' after defined period of inactivity.
        :param data: Device data, a JSON object with an arbitrary structure.
        :param network: A Network object which includes name property to match.
        In case when the target network is protected with a key, the key value must also be included.
        :return: None
        """
        jsonToSend = {"id": id,
                      "name": name,
                      "deviceClass": deviceClass.ToDictionary()}

        if key:
            jsonToSend["key"] = key

        if status:
            jsonToSend["status"] = status

        if data:
            jsonToSend["data"] = data

        if network:
            jsonToSend["network"] = network.ToDictionary()

        try:
            requests.put(url=self.url+"/device/"+id,
                         json=jsonToSend,
                         auth=(self.login, self.password))
        except:
            pass

    def DeleteDevice(self, id):
        """
        Deletes an existing device.
        :param id: Device unique identifier.
        :return: None
        """

        try:
            requests.delete(url=self.url+"/device/"+id,
                            auth=(self.login, self.password))
        except:
            pass

    def GetDeviceEquipment(self, id):
        """
        Gets current state of device equipment.
        The equipment state is tracked by framework and it could be updated by sending 'equipment' notification with the following parameters:
        equipment: equipment code
        parameters: current equipment state
        :param id: Device unique identifier.
        :return: List of EquipmentState objects.
        """

        r = None

        try:
            r = requests.get(url=self.url+"/device/"+id+"/equipment",
                             auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 200:
            return [EquipmentState.EquipmentState.FromDictionary(equipmentStateDict) for equipmentStateDict in json.loads(r.text)]

        return None


    def ListNetworks(self, name=None, namePattern=None, sortField=None, sortOrder=None, take=None, skip=None):
        """
        Gets list of device networks.
        The result list is limited to networks the client has access to.
        :param name: Filter by network name.
        :param namePattern: Filter by network name pattern.
        :param sortField: Result list sort field. Available values are ID and Name.
        :param sortOrder: Result list sort order. Available values are ASC and DESC.
        :param take: Number of records to take from the result list.
        :param skip: Number of records to skip from the result list.
        :return: List of NetworkLite objects.
        """
        r = None

        try:
            r = requests.get(url=self.url+"/network",
                             json={"name": name,
                                   "namePattern": namePattern,
                                   "sortField": sortField,
                                   "sortOrder": sortOrder,
                                   "take": take,
                                   "skip": skip},
                             auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 200:
            return [NetworkLite.NetworkLite.FromDictionary(networkDict) for networkDict in json.loads(r.text)]

        return None

    def GetNetwork(self, id):
        """
        Gets information about device network and its devices.
        :param id: Network identifier.
        :return: NetworkFull object.
        """

        r = None

        try:
            r = requests.get(url=self.url+"/network/"+str(id),
                             auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 200:
            return NetworkFull.NetworkFull.FromDictionary(json.loads(r.text))

        return None

    def InsertNetwork(self, name, key=None, description=None):
        """
        Creates new device network.
        :param name: Network display name.
        :param key: Optional key that is used to protect the network from unauthorized device registrations. When defined, devices will need to pass the key in order to register to the current network.
        :param description: Network description.
        :return: Id of created network.
        """

        jsonToSend={"name": name}

        if key:
            jsonToSend["key"] = key

        if description:
            jsonToSend["description"] = description

        r = None

        try:
            r = requests.post(url=self.url+"/network",
                             json=jsonToSend,
                             auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 201:
            return json.loads(r.text)["id"]

        return None

    def UpdateNetwork(self, id, name=None, key=None, description=None):
        """
        Updates an existing device network.
        :param id: Network identifier.
        :param name: Network display name.
        :param key: Optional key that is used to protect the network from unauthorized device registrations. When defined, devices will need to pass the key in order to register to the current network.
        :param description: Network description.
        :return: None.
        """

        jsonToSend={"id": id}

        if name:
            jsonToSend["name"] = name

        if key:
            jsonToSend["key"] = key

        if description:
            jsonToSend["description"] = description

        try:
            requests.put(url=self.url+"/network/"+str(id),
                         json=jsonToSend,
                         auth=(self.login, self.password))
        except:
            pass

    def DeleteNetwork(self, id):
        """
        Deletes an existing device network.
        :param id: Network identifier.
        :return: None.
        """

        try:
            requests.delete(url=self.url+"/network/"+str(id),
                            auth=(self.login, self.password))
        except:
            pass

    def ListOAuthClients(self, name=None, namePattern=None, domain=None, oauthId=None, sortField=None, sortOrder=None, take=None, skip=None):
        """
        Gets list of OAuth clients.
        :param name: Filter by client name.
        :param namePattern: Filter by client name pattern.
        :param domain: Filter by domain.
        :param oauthId: Filter by OAuth client ID.
        :param sortField: Result list sort field. Available values are ID, Name, Domain and OAuthID.
        :param sortOrder: Result list sort order. Available values are ASC and DESC.
        :param take: Number of records to take from the result list.
        :param skip: Number of records to skip from the result list.
        :return: List of OAuthClient objects.
        """
        jsonToSend={}

        if name:
            jsonToSend["name"] = name

        if namePattern:
            jsonToSend["namePattern"] = namePattern

        if domain:
            jsonToSend["domain"] = domain

        if oauthId:
            jsonToSend["oauthId"] = oauthId

        if sortField:
            jsonToSend["sortField"] = sortField

        if sortOrder:
            jsonToSend["sortOrder"] = sortOrder

        if take:
            jsonToSend["take"] = take

        if skip:
            jsonToSend["skip"] = skip

        r = None

        try:
            r = requests.get(url=self.url+"/oauth/client",
                             json=jsonToSend)
        except:
            return None

        if r.status_code == 200:

            return [OAuthClient.OAuthClient.FromDictionary(oauthClientDict) for oauthClientDict in json.loads(r.text)]

        return None

    def GetOAuthClient(self, id):
        """
        Gets information about OAuth client.
        :param id: OAuth client identifier.
        :return: OAuthClient object.
        """

        r = None

        try:
            r = requests.get(url=self.url+"/oauth/client/"+str(id))
        except:
            return None

        if r.status_code == 200:
            return OAuthClient.OAuthClient.FromDictionary(json.loads(r.text))

        return None

    def InsertOAuthClient(self, name, domain, redirectUri, oauthId, subnet=None):
        """
        Creates new OAuth client.
        :param name: Client display name.
        :param domain: Client domain allowed for API access.
        :param redirectUri: Client OAuth redirect URI.
        :param oauthId: Client OAuth ID.
        :param subnet: Client IP subnet allowed for API access.
        :return: OAuthClientCreatedResponse object.
        """
        jsonToSend={"name": name,
                    "domain": domain,
                    "redirectUri": redirectUri,
                    "oauthId": oauthId}

        if subnet:
            jsonToSend["subnet"] = subnet

        r = None

        try:
            r = requests.post(url=self.url+"/oauth/client",
                              json=jsonToSend,
                              auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 201:
            return OAuthClientCreatedResponse.OAuthClientCreatedResponse.FromDictionary(json.loads(r.text))

        return None

    def UpdateOAuthClient(self, id, name=None, domain=None, subnet=None, redirectUri=None, oauthId=None):
        """
        Updates an existing OAuth client.
        :param id: OAuth client identifier.
        :param name: Client display name.
        :param domain: Client domain allowed for API access.
        :param subnet: Client IP subnet allowed for API access.
        :param redirectUri: Client OAuth redirect URI.
        :param oauthId: Client OAuth ID.
        :return: None.
        """
        jsonToSend={"id": id}

        if name:
            jsonToSend["name"] = name

        if domain:
            jsonToSend["domain"] = domain

        if subnet:
            jsonToSend["subnet"] = subnet

        if redirectUri:
            jsonToSend["redirectUri"] = redirectUri

        if oauthId:
            jsonToSend["oauthId"] = oauthId

        try:
            requests.put(url=self.url+"/oauth/client/"+str(id),
                         json=jsonToSend,
                         auth=(self.login, self.password))
        except:
            pass

    def DeleteOAuthClient(self, id):
        """
        Deletes an existing OAuth client.
        :param id: OAuth client identifier.
        :return: None.
        """

        try:
            print requests.delete(url=self.url+"/oauth/client/"+str(id),
                            auth=(self.login, self.password)).text
        except:
            pass

    def ListOAuthGrants(self, userId, start=None, end=None, clientOAuthId=None, type=None, scope=None,
                        redirectUri=None, accessType=None, sortField=None, sortOrder=None, take=None, skip=None):
        """
        Gets list of OAuth grants.
        :param userId: User identifier. Use the 'current' keyword to list OAuth grants of the current user.
        :param start: Filter by grant start timestamp (UTC).
        :param end: Filter by grant start timestamp (UTC).
        :param clientOAuthId: Filter by OAuth client OAuth identifier.
        :param type: Filter by OAuth grant type.
        :param scope: Filter by OAuth scope.
        :param redirectUri: Filter by OAuth redirect URI.
        :param accessType: Filter by access type.
        :param sortField: Result list sort field. Available values are Timestamp (default).
        :param sortOrder: Result list sort order. Available values are ASC and DESC.
        :param take: Number of records to take from the result list.
        :param skip: Number of records to skip from the result list.
        :return: List of OAuthGrant objects..
        """

        jsonToSend={"userId": userId}

        if start:
            jsonToSend["start"] = start

        if end:
            jsonToSend["end"] = end

        if clientOAuthId:
            jsonToSend["clientOAuthId"] = clientOAuthId

        if type:
            jsonToSend["type"] = type

        if scope:
            jsonToSend["scope"] = scope

        if redirectUri:
            jsonToSend["redirectUri"] = redirectUri

        if accessType:
            jsonToSend["accessType"] = accessType

        if sortField:
            jsonToSend["sortField"] = sortField

        if sortOrder:
            jsonToSend["sortOrder"] = sortOrder

        if take:
            jsonToSend["take"] = take

        if skip:
            jsonToSend["skip"] = skip

        r = None

        try:
            r = requests.get(url=self.url+"/user/"+str(userId)+"/oauth/grant",
                             json=jsonToSend,
                             auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 200:

            return [OAuthGrant.OAuthGrant.FromDictionary(oAuthGrantDict) for oAuthGrantDict in json.loads(r.text)]

        return None

    def GetOAuthGrant(self, userId, id):
        """
        Gets information about OAuth grant.
        :param userId: User identifier. Use the 'current' keyword to get OAuth grant of the current user.
        :param id: OAuth grant identifier.
        :return: OAuthGrant object.
        """
        r = None

        try:
            r = requests.get(url=self.url+"/user/"+str(userId)+"/oauth/grant/"+str(id),
                             auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 200:
            return OAuthGrant.OAuthGrant.FromDictionary(json.loads(r.text))

        return None

    def InsertOAuthGrant(self, userId, client, type, redirectUri, scope, accessType=None, networkIds=None):
        """
        Creates new OAuth grant.
        :param userId: User identifier. Use the 'current' keyword to create OAuth grant for the current user.
        :param client: A OAuthClient object which includes oauthId property to match.
        :param type: OAuth grant type. STRING!
        Code: Authorization Code grant
        Token: Implicit grant
        Password: Password Credentials grant
        :param redirectUri: OAuth redirect URI specified during authorization.
        :param scope: Requested OAuth scope. The scope should include a space-delimited list of required access key permissions.
        :param accessType: Grant access type. STRING! Available values:
        Online: Access is requested to a limited period of time
        Offline: Assess is requested for an unlimited period of time
        :param networkIds: A collection of network identifiers requested for access. Set to null to request access for all accessible networks.
        :return: OAuthGrantCreatedResponse object.
        """
        jsonToSend={"userId": userId,
                    "client": client.ToDictionary(),
                    "type": type,
                    "redirectUri": redirectUri,
                    "scope": scope}

        if accessType:
            jsonToSend["accessType"] = accessType

        if networkIds:
            jsonToSend["networkIds"] = networkIds

        r = None

        try:
            r = requests.post(url=self.url+"/user/"+str(userId)+"/oauth/grant",
                              json=jsonToSend,
                              auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 201:
            return OAuthGrantCreatedResponse.OAuthGrantCreatedResponse.FromDictionary(json.loads(r.text))

        return None

    def UpdateOAuthGrant(self, userId, id, client=None, type=None, accessType=None, redirectUri=None, scope=None, networkIds=None):
        """
        Updates an existing OAuth grant.
        :param userId: User identifier. Use the 'current' keyword to update OAuth grant of the current user.
        :param id: OAuth grant identifier.
        :param client: A OAuthClient object which includes oauthId property to match.
        :param type: OAuth grant type.
        Code: Authorization Code grant
        Token: Implicit grant
        Password: Password Credentials grant
        :param accessType: Grant access type. Available values:
        Online: Access is requested to a limited period of time
        Offline: Assess is requested for an unlimited period of time
        :param redirectUri: OAuth redirect URI specified during authorization.
        :param scope: Requested OAuth scope. The scope should include a space-delimited list of required access key permissions.
        :param networkIds: 	A collection of network identifiers requested for access. Set to null to request access for all accessible networks.
        :return: OAuthGrantCreatedResponse object.
        """
        jsonToSend={"userId": userId,
                    "id": id}

        if client:
            jsonToSend["client"] = client.ToDictionary()

        if type:
            jsonToSend["type"] = type

        if accessType:
            jsonToSend["accessType"] = accessType

        if redirectUri:
            jsonToSend["redirectUri"] = redirectUri

        if scope:
            jsonToSend["scope"] = scope

        if networkIds:
            jsonToSend["networkIds"] = networkIds

        r = None

        try:
            r = requests.put(url=self.url+"/user/"+str(userId)+"/oauth/grant/"+str(id),
                             json=jsonToSend,
                             auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 200:
            return OAuthGrantCreatedResponse.OAuthGrantCreatedResponse.FromDictionary(json.loads(r.text))

        return None

    def DeleteOAuthGrant(self, userId, id):
        """
        Deletes an existing OAuth grant.
        :param userId: User identifier. Use the 'current' keyword to delete OAuth grant of the current user.
        :param id: 	OAuth grant identifier.
        :return: None.
        """

        try:
            requests.delete(url=self.url+"/user/"+str(userId)+"/oauth/grant/"+str(id),
                            auth=(self.login, self.password))
        except:
            pass

    def ListUsers(self, login=None, loginPattern=None, role=None, status=None, sortField=None, sortOrder=None, take=None, skip=None):
        """
        Gets list of users.
        :param login: Filter by user login.
        :param loginPattern: Filter by user login pattern.
        :param role: Filter by user role. 0 is Administrator, 1 is Client.
        :param status: Filter by user status. 0 is Active, 1 is Locked Out, 2 is Disabled.
        :param sortField: Result list sort field. Available values are ID and Login.
        :param sortOrder: Result list sort order. Available values are ASC and DESC.
        :param take: Number of records to take from the result list.
        :param skip: Number of records to skip from the result list.
        :return: List of UserShort objects.
        """
        jsonToSend={}

        if login:
            jsonToSend["login"] = login

        if loginPattern:
            jsonToSend["loginPattern"] = loginPattern

        if role:
            jsonToSend["role"] = role

        if status:
            jsonToSend["status"] = status

        if sortField:
            jsonToSend["sortField"] = sortField

        if sortOrder:
            jsonToSend["sortOrder"] = sortOrder

        if take:
            jsonToSend["take"] = take

        if skip:
            jsonToSend["skip"] = skip

        r = None

        try:
            r = requests.get(url=self.url+"/user",
                             json=jsonToSend,
                             auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 200:
            return [UserShort.UserShort.FromDictionary(userDict) for userDict in json.loads(r.text)]

        return None

    def GetUser(self, id):
        """
        Gets information about user and its assigned networks.
        Only administrators are allowed to get information about any user. User-level accounts can only retrieve information about themselves.
        :param id: User identifier. Use the 'current' keyword to get information about the current user.
        :return: User object.
        """

        r = None

        try:
            r = requests.get(url=self.url+"/user/"+str(id),
                             auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 200:
            return User.User.FromDictionary(json.loads(r.text))

        return None

    def InsertUser(self, login, role, status, password, facebookLogin=None, googleLogin=None, githubLogin=None):
        """
        Gets information about user and its assigned networks.
        Only administrators are allowed to get information about any user. User-level accounts can only retrieve information about themselves.
        :param login: User login using during authentication.
        :param role: User role. Available values:
        0: Administrator role
        1: Client role
        :param status: User status. Available values:
        0: The user is active
        1: The user has been locked out due to invalid login attempts
        2: The user has been disabled
        3: The user has been deleted
        :param password: User password
        :param facebookLogin: User Facebook login (for OAuth authentication).
        :param googleLogin: User Google login (for OAuth authentication).
        :param githubLogin: User Github login (for OAuth authentication).
        :return: UserCreatedResponse object.
        """
        jsonToSend={"login": login,
                    "role": role,
                    "status": status,
                    "password": password}

        if facebookLogin:
            jsonToSend["facebookLogin"] = facebookLogin

        if googleLogin:
            jsonToSend["googleLogin"] = googleLogin

        if githubLogin:
            jsonToSend["githubLogin"] = githubLogin

        r = None

        try:
            r = requests.post(url=self.url+"/user",
                              json=jsonToSend,
                              auth=(self.login, self.password))
        except:
            return None

        print r.text

        if r.status_code == 201:
            return UserCreatedResponse.UserCreatedResponse.FromDictionary(json.loads(r.text))

        return None

    def UpdateUser(self, id, login=None, facebookLogin=None, googleLogin=None, githubLogin=None,
                   role=None, status=None, password=None, oldPassword=None):
        """
        Updates an existing user.
        Only administrators are allowed to update any property of any user. User-level accounts can only change their own password in case:
        They already have a password.
        They provide a valid current password in the 'oldPassword' property.
        :param id: User identifier. Use the 'current' keyword to update information of the current user.
        :param login: 	User login using during authentication.
        :param facebookLogin: User Facebook login (for OAuth authentication).
        :param googleLogin: User Google login (for OAuth authentication).
        :param githubLogin: User Github login (for OAuth authentication).
        :param role: User role. Available values:
        0: Administrator role
        1: Client role
        :param status: User status. Available values:
        0: The user is active
        1: The user has been locked out due to invalid login attempts
        2: The user has been disabled
        3: The user has been deleted
        :param password: User new password
        :param oldPassword: User current password (for non-administrative password changing functionality only)
        :return: None.
        """
        jsonToSend={}

        if login:
            jsonToSend["login"] = login

        if facebookLogin:
            jsonToSend["facebookLogin"] = facebookLogin

        if googleLogin:
            jsonToSend["googleLogin"] = googleLogin

        if githubLogin:
            jsonToSend["githubLogin"] = githubLogin

        if role:
            jsonToSend["role"] = role

        if status:
            jsonToSend["status"] = status

        if password:
            jsonToSend["password"] = password

        if oldPassword:
            jsonToSend["oldPassword"] = oldPassword

        try:
            requests.put(url=self.url+"/user/"+str(id),
                         json=jsonToSend,
                         auth=(self.login, self.password))
        except:
            pass

    def DeleteUser(self, id):
        """
        Deletes an existing user.
        :param id: User identifier.
        :return: None.
        """

        try:
            requests.delete(url=self.url+"/user/"+str(id),
                            auth=(self.login, self.password))
        except:
            pass

    def GetUserNetwork(self, id, networkId):
        """
        Gets information about user/network association.
        :param id: 	User identifier.
        :param networkId: Network identifier.
        :return: NetworkLite object.
        """

        r = None

        try:
            r = requests.get(url=self.url+"/user/"+str(id)+"/network/"+str(networkId),
                             auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 200:
            return NetworkLite.NetworkLite.FromDictionary(json.loads(r.text)["network"])

        return None

    def AssignUserNetwork(self, id, networkId):
        """
        Associates network with the user.
        :param id: User identifier.
        :param networkId: 	Network identifier.
        :return: None.
        """

        try:
            requests.put(url=self.url+"/user/"+str(id)+"/network/"+str(networkId),
                         auth=(self.login, self.password))
        except:
            pass

    def UnassignUserNetwork(self, id, networkId):
        """
        Removes association between network and user.
        :param id: User identifier.
        :param networkId: Network identifier.
        :return: None.
        """

        try:
            requests.delete(url=self.url+"/user/"+str(id)+"/network/"+str(networkId),
                         auth=(self.login, self.password))
        except:
            pass

    def QueryDeviceCommands(self, deviceGuid, start=None, end=None, command=None, status=None, sortField=None, sortOrder=None,
                            take=None, skip=None):
        """
        Queries device commands.
        :param deviceGuid: Device unique identifier.
        :param start: Filter by command start timestamp (UTC).
        :param end: Filter by command end timestamp (UTC).
        :param command: Filter by command name.
        :param status: Filter by command status.
        :param sortField: Result list sort field. Available values are Timestamp (default), Command and Status.
        :param sortOrder: Result list sort order. Available values are ASC and DESC.
        :param take: Number of records to take from the result list (default is 1000).
        :param skip: Number of records to skip from the result list.
        :return: List of DeviceCommand objects.
        """

        jsonToSend = {}

        if start:
            jsonToSend["start"] = start

        if end:
            jsonToSend["end"] = end

        if command:
            jsonToSend["command"] = command

        if status:
            jsonToSend["status"] = status

        if sortField:
            jsonToSend["sortField"] = sortField

        if sortOrder:
            jsonToSend["sortOrder"] = sortOrder

        if take:
            jsonToSend["take"] = take

        if skip:
            jsonToSend["skip"] = skip

        r = None

        try:
            r = requests.get(url=self.url+"/device/"+str(deviceGuid)+"/command",
                             json=jsonToSend,
                             auth=(self.login, self.password))
        except:
            return None

        #print r.text

        if r.status_code == 200:
            return [DeviceCommand.DeviceCommand.FromDictionary(deviceCommandDict) for deviceCommandDict in json.loads(r.text)]

        return None

    def GetDeviceCommand(self, deviceGuid, id):
        """
        Gets information about device command.
        :param deviceGuid: Device unique identifier.
        :param id: Command identifier.
        :return: DeviceCommand object.
        """

        r = None

        try:
            r = requests.get(url=self.url+"/device/"+str(deviceGuid)+"/command/"+str(id),
                             auth=(self.login, self.password))
        except:
            return None

        #print r.text

        if r.status_code == 200:
            return DeviceCommand.DeviceCommand.FromDictionary(json.loads(r.text))

        return None

    def InsertDeviceCommand(self, deviceGuid, command, parameters=None, lifetime=None):
        """
        Creates new device command.
        :param deviceGuid: Device unique identifier.
        :param command: Command name.
        :param parameters: Command parameters, a JSON object with an arbitrary structure.
        :param lifetime: Command lifetime, a number of seconds until this command expires.
        :return: DeviceCommandCreatedResponse object.
        """
        jsonToSend = {"command": command}

        if parameters:
            jsonToSend["parameters"] = parameters

        if lifetime:
            jsonToSend["lifetime"] = lifetime

        r = None

        try:
            r = requests.post(url=self.url+"/device/"+str(deviceGuid)+"/command",
                              json=jsonToSend,
                              auth=(self.login, self.password))
        except:
            return None

        #print r.text

        if r.status_code == 201:
            return DeviceCommandCreatedResponse.DeviceCommandCreatedResponse.FromDictionary(json.loads(r.text))

        return None

    def UpdateDeviceCommand(self, deviceGuid, id, status=None, result=None):
        """
        Updates an existing device command.
        :param deviceGuid: Device unique identifier.
        :param id: Device command identifier.
        :param status: Command status, as reported by device or related infrastructure.
        :param result: Command execution result, an optional value that could be provided by device.
        :return: None.
        """
        jsonToSend = {}

        if status:
            jsonToSend["status"] = status

        if result:
            jsonToSend["result"] = result

        try:
            requests.put(url=self.url+"/device/"+str(deviceGuid)+"/command/"+str(id),
                         json=jsonToSend,
                         auth=(self.login, self.password))
        except:
            pass

    def PollDeviceCommands(self, deviceGuid, timestamp=None, names=None, waitTimeout=None):
        """
        Polls new device commands.
        This method returns all device commands that were created after specified timestamp.
        In the case when no commands were found, the method blocks until new command is received. If no commands are received within the waitTimeout period, the server returns an empty response. In this case, to continue polling, the client should repeat the call with the same timestamp value.
        :param deviceGuid: Device unique identifier.
        :param timestamp: Timestamp of the last received command (UTC). If not specified, the server's timestamp is taken instead.
        :param names: Comma-separated list of commands names.
        :param waitTimeout: Waiting timeout in seconds (default: 30 seconds, maximum: 60 seconds). Specify 0 to disable waiting.
        :return: List of DeviceCommand objects.
        """
        r = None

        try:
            r = requests.get(url=self.url+"/device/%s/command/poll?timestamp=%s&names=%s&waitTimeout=%s" %
                                          (str(deviceGuid),
                                           str(timestamp) if timestamp else "",
                                           str(names) if names else "",
                                           str(waitTimeout) if waitTimeout else ""),
                             auth=(self.login, self.password))
        except:
            return None

        #print r.text

        if r.status_code == 200:
            return [DeviceCommand.DeviceCommand.FromDictionary(deviceCommandDict) for deviceCommandDict in json.loads(r.text)]

        return None

    def WaitDeviceCommand(self, deviceGuid, id, waitTimeout=None):
        """
        Waits for a command to be processed.
        This method returns a command only if it has been processed by a device.
        In the case when command is not processed, the method blocks until device acknowledges command execution. If the command is not processed within the waitTimeout period, the server returns an empty response. In this case, to continue polling, the client should repeat the call.
        :param deviceGuid: Device unique identifier.
        :param id: Command identifier.
        :param waitTimeout: Waiting timeout in seconds (default: 30 seconds, maximum: 60 seconds). Specify 0 to disable waiting.
        :return: DeviceCommand object.
        """
        r = None

        try:
            r = requests.get(url=self.url+"/device/%s/command/%s/poll?waitTimeout=%s" %
                                          (str(deviceGuid),
                                           str(id),
                                           str(waitTimeout) if waitTimeout else ""),
                             auth=(self.login, self.password))
        except:
            return None

        #print r.text

        if r.status_code == 200:
            return DeviceCommand.DeviceCommand.FromDictionary(json.loads(r.text))

        return None

    def PollManyDeviceCommands(self, deviceGuids=None, timestamp=None, names=None, waitTimeout=None):
        """
        Polls new device commands.
        This method returns all device commands that were created after specified timestamp.
        In the case when no commands were found, the method blocks until new command is received. If no commands are received within the waitTimeout period, the server returns an empty response. In this case, to continue polling, the client should repeat the call with the same timestamp value.
        :param deviceGuids: Comma-separated list of device unique identifiers.
        :param timestamp: Timestamp of the last received command (UTC). If not specified, the server's timestamp is taken instead.
        :param names: Comma-separated list of commands names.
        :param waitTimeout: Waiting timeout in seconds (default: 30 seconds, maximum: 60 seconds). Specify 0 to disable waiting.
        :return: List of DeviceCommand objects.
        """
        r = None

        try:
            r = requests.get(url=self.url+"/device/command/poll?deviceGuids=%s&timestamp=%s&names=%s&waitTimeout=%s" %
                                          (str(deviceGuids) if deviceGuids else "",
                                           str(timestamp) if timestamp else "",
                                           str(names) if names else "",
                                           str(waitTimeout) if waitTimeout else ""),
                             auth=(self.login, self.password))
        except:
            return None

        #print r.text

        if r.status_code == 200:
            return json.loads(r.text)

        return None

    def QueryDeviceNotifications(self, deviceGuid, start=None, end=None, notification=None, gridInterval=None,
                                 sortField=None, sortOrder=None, take=None, skip=None):
        """
        Queries device notifications.
        :param deviceGuid: Device unique identifier.
        :param start: Filter by notification start timestamp (UTC).
        :param end: Filter by notification end timestamp (UTC).
        :param notification: Filter by notification name.
        :param gridInterval: Filter notifications to retrieve maximum one notification of the same type within the specified grid interval (interval is measured in seconds).
        :param sortField: Result list sort field. Available values are Timestamp (default) and Notification.
        :param sortOrder: Result list sort order. Available values are ASC and DESC.
        :param take: Number of records to take from the result list (default is 1000).
        :param skip: Number of records to skip from the result list.
        :return: List of DeviceNotification objects.
        """
        jsonToSend = {}

        if start:
            jsonToSend["start"] = start

        if end:
            jsonToSend["end"] = end

        if notification:
            jsonToSend["notification"] = notification

        if gridInterval:
            jsonToSend["gridInterval"] = gridInterval

        if sortField:
            jsonToSend["sortField"] = sortField

        if sortOrder:
            jsonToSend["sortOrder"] = sortOrder

        if take:
            jsonToSend["take"] = take

        if skip:
            jsonToSend["skip"] = skip

        r = None

        try:
            r = requests.get(url=self.url+"/device/"+str(deviceGuid)+"/notification",
                             json=jsonToSend,
                             auth=(self.login, self.password))
        except:
            return None

        print r.text

        if r.status_code == 200:
            return [DeviceNotification.DeviceNotification.FromDictionary(deviceNotificationDict) for deviceNotificationDict in json.loads(r.text)]

        return None

    def GetDeviceNotification(self, deviceGuid, id):
        """
        Gets information about device notification.
        :param deviceGuid: Device unique identifier.
        :param id: Notification identifier.
        :return: DeviceNotification object.
        """
        r = None

        try:
            r = requests.get(url=self.url+"/device/"+str(deviceGuid)+"/notification/"+str(id),
                             auth=(self.login, self.password))
        except:
            return None

        print r.text

        if r.status_code == 200:
            return DeviceNotification.DeviceNotification.FromDictionary(json.loads(r.text))

        return None

    #Device MUST be connected to network!!!
    def InsertDeviceNotification(self, deviceGuid, notification, parameters=None):
        """
        Creates new device notification.
        :param deviceGuid: Device unique identifier.
        :param notification: Notification name.
        :param parameters: Notification parameters, a JSON object with an arbitrary structure.
        :return: DeviceNotificationCreatedResponse object.
        """
        jsonToSend = {"notification": notification}

        if parameters:
            jsonToSend["parameters"] = parameters

        r = None

        try:
            r = requests.post(url=self.url+"/device/"+str(deviceGuid)+"/notification",
                              json=jsonToSend,
                              auth=(self.login, self.password))
        except:
            return None

        #print r.text
        #print "ok"

        if r.status_code == 201:
            return DeviceNotificationCreatedResponse.DeviceNotificationCreatedResponse.FromDictionary(json.loads(r.text))

        return None

    def PollDeviceNotifications(self, deviceGuid, timestamp=None, names=None, waitTimeout=None):
        """
        Polls new device notifications.
        This method returns all device notifications that were created after specified timestamp.
        In the case when no notifications were found, the method blocks until new notification is received. If no notifications are received within the waitTimeout period, the server returns an empty response. In this case, to continue polling, the client should repeat the call with the same timestamp value.
        :param deviceGuid: Device unique identifier.
        :param timestamp: Timestamp of the last received notification (UTC). If not specified, the server's timestamp is taken instead.
        :param names: Comma-separated list of notification names.
        :param waitTimeout: Waiting timeout in seconds (default: 30 seconds, maximum: 60 seconds). Specify 0 to disable waiting.
        :return: List of DeviceNotification objects.
        """
        r = None

        try:
            r = requests.get(url=self.url+"/device/%s/notification/poll?timestamp=%s&names=%s&waitTimeout=%s" %
                                          (str(deviceGuid),
                                           str(timestamp) if timestamp else "",
                                           str(names) if names else "",
                                           str(waitTimeout) if waitTimeout else ""),
                             auth=(self.login, self.password))
        except:
            return None

        print r.text

        if r.status_code == 200:
            return [DeviceNotification.DeviceNotification.FromDictionary(deviceNotificationDict) for deviceNotificationDict in json.loads(r.text)]

        return None

    def PollManyDeviceNotifications(self, deviceGuids=None, timestamp=None, names=None, waitTimeout=None):
        """
        Polls new device notifications.
        This method returns all device notifications that were created after specified timestamp.
        In the case when no notifications were found, the method blocks until new notification is received. If no notifications are received within the waitTimeout period, the server returns an empty response. In this case, to continue polling, the client should repeat the call with the same timestamp value.
        :param deviceGuids: Comma-separated list of device unique identifiers.
        :param timestamp: Timestamp of the last received notification (UTC). If not specified, the server's timestamp is taken instead.
        :param names: Comma-separated list of notification names.
        :param waitTimeout: Waiting timeout in seconds (default: 30 seconds, maximum: 60 seconds). Specify 0 to disable waiting.
        :return: List of DeviceNotification objects.
        """
        r = None

        try:
            r = requests.get(url=self.url+"/device/notification/poll?deviceGuids=%s&timestamp=%s&names=%s&waitTimeout=%s" %
                                          (str(deviceGuids) if deviceGuids else "",
                                           str(timestamp) if timestamp else "",
                                           str(names) if names else "",
                                           str(waitTimeout) if waitTimeout else ""),
                             auth=(self.login, self.password))
        except:
            return None

        if r.status_code == 200:
            return json.loads(r.text)

        return None