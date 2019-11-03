
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebDriverFactory():

    def __init__(self, browser):

        self.browser = browser

    def getWebDriverInstance(self):

        mobile_emulation = {"deviceName": "Nexus 4"}
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        baseURL = "https://essayshark.com/"
        AdminURL = "https://esdirect.zae.cc/"

        if self.browser == "firefox":
            driver = webdriver.Firefox()
            driver.get(AdminURL)
        elif self.browser == "chrome":
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(baseURL)
        else:
            driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(5)
        return driver