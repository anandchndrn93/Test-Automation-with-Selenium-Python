from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WaitUtil:

    def __init__(self, driver):
        self.driver = driver

    def waitforVisibilityofElement(self, *element):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(*element))

    def waitForElementToBeClickable(self, *element):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(*element))

    def waitForElementToBePresent(self, *element):
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(*element))
