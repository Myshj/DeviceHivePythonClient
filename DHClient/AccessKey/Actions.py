from ThirdParty.enum import Enum

class Actions(Enum):

    GetNetwork = 1,
    GetDevice = 2,
    GetDeviceState = 3,
    GetDeviceNotification = 4,
    GetDeviceCommand = 5,
    RegisterDevice = 6,
    CreateDeviceNotification = 7,
    CreateDeviceCommand = 8,
    UpdateDeviceCommand = 9