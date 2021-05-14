import time

from selenium.common.exceptions import NoAlertPresentException


class ActionUtil:
    def __init__(self, driver):
        self.driver = driver

    def getAlert(self):
        alert = None
        timeout = 0
        while (timeout + 1) < 10:
            try:
                time.sleep(1)
                alert = self.driver.switch_to.alert
                break
            except NoAlertPresentException as ex:
                # ex.stacktrace
                print("retry count: " + timeout)
            # Alert not present

        return alert

    def scrollIntoView(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
