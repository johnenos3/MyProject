"""
@package utilitie

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver
from traceback import print_stack

class TestStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")
            self.screenShot(resultMessage)
            print_stack()

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a tests case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a tests case
        This needs to be called at least once in a tests case
        This should be final tests status of the tests case
        """
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName +  " ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True