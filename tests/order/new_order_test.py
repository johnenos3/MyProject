from sdfds.home.login_page import LoginPage
from sdfds.order.order_page import OrderPage
from utilitie.teststatus import TestStatus
from sdfds.home.navigation_page import NavigationPage
import unittest
import pytest
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class OrderTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)
        self.ord = OrderPage(self.driver)

    def setUp(self):
        self.nav.navigateToMainMenu()
        self.nav.clickBanner()
        self.nav.navigateToNewOrder()

    def test_checkUploadFile(self):
        time.sleep(3)
        self.ord.uploadFile("C:\\Users\\Professional\\Pictures\\Saved Pictures\\allannon.jpg")
        time.sleep(5)




















