import unittest

from DHClient import DHClient


class Test_DHClient(unittest.TestCase):

    def setUp(self):

        self.url = "http://localhost/api/rest"

        self.login = "dhadmin"

        self.password = "dhadmin_#911"

        self.dhClient = DHClient.DHClient(self.url, self.login, self.password)

    def test_init(self):

        self.assertEqual(self.dhClient.url, self.url, "URL hasn't been correctly assigned.")

        self.assertEqual(self.dhClient.login, self.login, "Login hasn't been correctly assigned.")

        self.assertEqual(self.dhClient.password, self.password, "Password hasn't been correctly assigned.")

    def test_GetInfo(self):

        self.assertNotEqual(self.dhClient.GetApiInfo(), None)

    def test_ListAccessKeys(self):

        self.assertNotEqual(self.dhClient.ListAccessKeys(1), None)

        print repr(self.dhClient.ListAccessKeys.__doc__)

    def test_GetAccessKey(self):

        self.assertNotEqual(self.dhClient.GetAccessKey(1, 1), None)

    def test_InsertAccessKey(self):

        self.assertNotEqual(self.dhClient.InsertAccessKey(1, "test11122211211"), None)

    def test_UpdateAccessKey(self):

        self.assertEqual(self.dhClient.UpdateAccessKey(1, 15), None)

    def test_DeleteAccessKey(self):

        self.assertEqual(self.dhClient.DeleteAccessKey(1, 15), None)

    def test_GetAuthConfig(self):

        self.assertNotEqual(self.dhClient.GetAuthConfig(), None)

    def test_Login(self):

        self.assertNotEqual(self.dhClient.Login("password", "dhadmin", "dhadmin_#911"),None)

    def test_Logout(self):

        self.assertEqual(self.dhClient.Logout(), None)

    def test_ListDeviceClasses(self):

        self.assertNotEqual(len(self.dhClient.ListDeviceClasses()), 0)

    def test_GetDeviceClass(self):

        self.assertNotEqual(self.dhClient.GetDeviceClass(1), None)

    def test_InsertDeviceClass(self):

        self.assertEqual(self.dhClient.InsertDeviceClass("test", "0.1"), None)

    def test_UpdateDeviceClass(self):

        self.assertEqual(self.dhClient.UpdateDeviceClass(2, "test1"), None)

    def test_DeleteDeviceClass(self):

        self.assertEqual(self.dhClient.DeleteDeviceClass(2), None)

    def test_ListNDevices(self):

        self.assertNotEqual(self.dhClient.ListDevices(), None)

    def test_GetDevice(self):

        self.assertNotEqual(self.dhClient.GetDevice("e50d6085-2aba-48e9-b1c3-73c673e414be"), None)

    def test_RegisterDevice(self):

        self.assertEqual(self.dhClient.RegisterDevice("4", "testDevice1", deviceClass=self.dhClient.GetDeviceClass(1)), None)

    def test_DeleteDevice(self):

        self.assertEqual(self.dhClient.DeleteDevice("3"), None)

    def test_GetDeviceEquipment(self):

        self.assertNotEqual(self.dhClient.GetDeviceEquipment("e50d6085-2aba-48e9-b1c3-73c673e414be"), None)

    def test_ListNetworks(self):

        self.assertNotEqual(self.dhClient.ListNetworks(), None)

    def test_GetNetwork(self):

        self.assertNotEqual(self.dhClient.GetNetwork(1), None)

    def test_RegisterNetwork(self):

        self.assertNotEqual(self.dhClient.InsertNetwork("test11"), None)

    def test_UpdateNetwork(self):

        self.assertEqual(self.dhClient.UpdateNetwork(3), None)

    def test_DeleteNetwork(self):

        self.assertEqual(self.dhClient.DeleteNetwork(3), None)

    def test_ListOAuthClients(self):

        self.assertNotEqual(self.dhClient.ListOAuthClients(), None)

    def test_GetOAuthClient(self):

        self.assertNotEqual(self.dhClient.GetOAuthClient(3), None)

    def test_InsertOAuthClient(self):

        self.assertNotEqual(self.dhClient.InsertOAuthClient("test", "google.com", "google.com", "maus"), None)

    def test_UpdateOAuthClient(self):

        self.assertEqual(self.dhClient.UpdateOAuthClient(1, name="mysha"), None)

    def test_DeleteOAuthClient(self):

        self.assertEqual(self.dhClient.DeleteOAuthClient(2), None)

    def test_ListOAuthGrants(self):

        self.assertNotEqual(self.dhClient.ListOAuthGrants(1), None)

    def test_GetOAuthGrant(self):

        self.assertNotEqual(self.dhClient.GetOAuthGrant(1, 1), None)

    def test_InsertOAuthGrant(self):

        self.assertNotEqual(self.dhClient.InsertOAuthGrant(userId=1,
                                                           client=self.dhClient.GetOAuthClient(3),
                                                           type="Code",
                                                           redirectUri="google.com",
                                                           scope="GetNetwork"), None)

    def test_UpdateOAuthGrant(self):

        self.assertNotEqual(self.dhClient.UpdateOAuthGrant(1, 3), None)

    def test_DeleteOAuthGrant(self):

        self.assertEqual(self.dhClient.DeleteOAuthGrant(1, 3), None)

    def test_ListUsers(self):

        self.assertNotEqual(self.dhClient.ListUsers(), None)

    def test_GetUser(self):

        self.assertNotEqual(self.dhClient.GetUser(1), None)

    def test_InsertUser(self):

        self.assertNotEqual(self.dhClient.InsertUser(login="login111222221",
                                                     role=1,
                                                     status=0,
                                                     password="password",
                                                     facebookLogin="loginF1"), None)

    def test_UpdateUser(self):

        self.assertEqual(self.dhClient.UpdateUser(1), None)

    def test_DeleteUser(self):

        self.assertEqual(self.dhClient.DeleteUser(3), None)

    def test_GetUserNetwork(self):

        self.assertNotEqual(self.dhClient.GetUserNetwork(1, 1), None)

    def test_AssignUserNetwork(self):

        self.assertEqual(self.dhClient.AssignUserNetwork(1, 1), None)

    def test_UnassignUserNetwork(self):

        self.assertEqual(self.dhClient.UnassignUserNetwork(1, 1), None)

    def test_ListDeviceCommands(self):

        self.assertNotEqual(self.dhClient.QueryDeviceCommands("1"), None)

    def test_GetDeviceCommand(self):

        self.assertNotEqual(self.dhClient.GetDeviceCommand("1", 2073896471), None)

    def test_InsertDeviceCommand(self):

        self.assertNotEqual(self.dhClient.InsertDeviceCommand("1", "test"), None)

    def test_UpdateDeviceCommand(self):

        self.assertNotEqual(self.dhClient.UpdateDeviceCommand("1", 2073896471, status="AAAAAAAA"), None)

    def test_PollDeviceCommands(self):

        self.assertNotEqual(self.dhClient.PollDeviceCommands("1", timestamp="2016-01-24T08:43:35.010"), None)

    def test_WaitDeviceCommand(self):

        self.assertNotEqual(self.dhClient.WaitDeviceCommand("1", 2073896471), None)

    def test_PollManyDeviceCommands(self):

        self.assertNotEqual(self.dhClient.PollManyDeviceCommands( timestamp="2016-01-24T08:43:35.010"), None)

    def test_QueryDeviceNotifications(self):

        self.assertNotEqual(self.dhClient.QueryDeviceNotifications("1"), None)

    def test_GetDeviceNotification(self):

        self.assertNotEqual(self.dhClient.GetDeviceNotification("1", 1), None)

    def test_InsertDeviceNotification(self):

        self.assertNotEqual(self.dhClient.InsertDeviceNotification("e50d6085-2aba-48e9-b1c3-73c673e414be", "test"), None)

    def test_PollDeviceNotifications(self):
        pass
        #self.assertNotEqual(self.dhClient.Po)


if __name__ == '__main__':
    unittest.main()
