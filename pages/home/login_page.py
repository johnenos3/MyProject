import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage
import time

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "//*[@id='id_esauth_myaccount_login_link']"
    _email_field = "//*[@id='id_esauth_login_field']"
    _password_field = "//*[@id='id_esauth_pwd_field']"
    _login_button = "//*[@id='id_esauth_login_button']"
    _menu_logout = "profile__item-logout"  # class

    _email_for_signUp = "input_email" #class
    _new_news = "//*[@id='latest-news-tab']/table/tbody//td[2]/b/a"
    _tab_News = "//*[@id='user_nav']/li[7]/a"
    _tab_Orders = "//*[@id='user_nav']/li[1]/a"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("header__select-status-title", locatorType="class")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//*[contains(text(),'This field is required')]", locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Essay")

    def logout(self):
        self.nav.navigateToMainMenu()
        self.nav.navigateToProfile()
        self.nav.clickBanner()
        self.webScroll("down")
        self.elementClick(locator=self._menu_logout, locatorType="class")

    def verifyLoginWRSuccessful(self):
        try:
            return self.isElementPresent("Orders", locatorType="link")
        except:
            print("I think we have news on page News")
        else:
            return self.isElementPresent("News ", locatorType="link")


    def verifyWRLoginTitle(self):
        a = "Available Orders - EssayShark.com"
        b = "News list | EssayShark.com"
        if self.verifyPageTitle(a):
            return True
        elif self.verifyPageTitle(b):
            while self.isElementPresent(locator=self._new_news, locatorType="xpath"):
                self.elementClick(locator=self._new_news, locatorType="xpath")
                time.sleep(5)
                self.elementClick(locator=self._tab_News, locatorType="xpath")
                time.sleep(5)
            self.elementClick(locator=self._tab_Orders, locatorType="xpath")
            return True
        else:
            return False



    def verifyLoginAdminSuccessful(self):
        result = self.getText("Welcome!", locatorType="link")
        return result

    def verifyAdminLoginTitle(self):
        return self.verifyPageTitle("EssayShark.com")

    def typeEmailForSignUP(self, email):
        self.sendKeys(email, locator=self._email_for_signUp, locatorType="class")












