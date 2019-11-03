import utilitie.custom_logger as cl
from sdfds.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage
import time


class SignUPPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators

    # SOF locators:
    _email_for_signUp = "input_email"  # class
    _type_of_paper_small = "sel_big" #class
    _select_type_of_paper = "//*[@id='id_esof_paper_type']/option[2]" #xpath
    _plus_page_small = "//*[@id='contentspin']/button[2]"  #xpath
    _minus_page_small = "//*[@id='contentspin']/button[1]" #xpath
    _get_deadline_form = "es-datepicker" #class
    __cookie_submit = "//*[@id='es-cookie-button-submit']" #xpath
    _set_deadline = "//*[@id='bodystart']/div[12]/table[5]/tbody/tr/td[1]" #xpath

    _deadline_calendar_small = "//*[@class='dp_daypicker']" #xpath

    _agree_gdpr = "gdpr-checkbox-custom-bgpolicy" # id
    _submit_SOF_button = "//*[@id='id_esof_subm']" #xpath

    _header_after_sign_up = "header__title-text" #class


    def enterEmailForSignUp(self, email):
        self.webScroll(direction="movetoSOF")
        self.elementClick(locator=self.__cookie_submit, locatorType="xpath")
        self.sendKeys(email, self._email_for_signUp, locatorType="class")

    def clickBlockTypeOfPaper(self):
        self.elementClick(locator=self._type_of_paper_small, locatorType="class")

    def selectTypeOfPaper(self):
        self.elementClick(locator=self._select_type_of_paper, locatorType="xpath")

    def openDeadlineForm(self):
        self.elementClick(locator=self._get_deadline_form, locatorType="class")

    def selectDeadline(self):
        self.elementClick(locator=self._set_deadline, locatorType="xpath")

    def agreeGDPR(self):
        self.elementClick(locator=self._agree_gdpr, locatorType="id")

    def submitRegistration(self):
        self.elementClick(locator=self._submit_SOF_button, locatorType="xpath")

    def testRegistration(self, email=""):
        self.enterEmailForSignUp(email)
        self.clickBlockTypeOfPaper()
        self.selectTypeOfPaper()
        self.openDeadlineForm()
        self.selectDeadline()
        self.agreeGDPR()
        self.submitRegistration()

    def verifyRegistrationSuccessful(self):
        result = self.isElementPresent("header__title-text", locatorType="class")
        return result



















