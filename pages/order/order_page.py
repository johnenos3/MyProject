import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class OrderPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _add_file = "lazyUpload-input" #class


    def uploadFile(self, file):
        self.webScroll("down")
        self.sendKeys(file, locator=self._add_file, locatorType="class")












