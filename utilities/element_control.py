import logging
import time

from selenium.common import InvalidArgumentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utilities.invalid_locator_exception import InvalidLocatorException


class ElementControl:
    element_log = logging.getLogger("demoblaze.element")

    def __init__(self, driver):
        self.driver = driver

    def type_text(self, data, *element):
        if len(element) == 1 and isinstance(element[0], str):
            self.driver.find_element(*self.locate(element[0])).send_keys(data)
        else:
            self.driver.find_element(*element).send_keys(data)
        self.element_log.info("Entered the value {} to the field {}".format(data, element))

    def clear_and_type(self, data, *element):
        if len(element) == 1 and isinstance(element[0], str):
            self.driver.find_element(*self.locate(element[0])).clear()
            self.type_text(data, *element)
        else:
            self.driver.find_element(*element).clear()
            self.type_text(data, *element)

        self.element_log.info("Entered the value {} to the field {}".format(data, element))

    def click_element(self, *element):
        if len(element) == 1 and isinstance(element[0], str):
            self.driver.find_element(*self.locate(element[0])).click()
        else:
            self.driver.find_element(*element).click()
        self.element_log.info("clicked on element {}".format(element))

    def get_text(self, *element):
        if len(element) == 1 and isinstance(element[0], str):
            text_val = self.driver.find_element(*self.locate(element[0])).text
        else:
            text_val = self.driver.find_element(*element).text
        self.element_log.info("text value of element {} is {}".format(element, text_val))
        return text_val

    def wait_for(self, time_out):
        try:
            time.sleep(time_out)
            self.element_log.info("waiting for {} seconds".format(time_out))
        except KeyboardInterrupt:
            self.element_log.info("there was an interruption")

    def wait_till_visible(self, element, timeout):
        wait = WebDriverWait(self.driver, timeout)
        if isinstance(element, str):
            wait.until(expected_conditions.visibility_of_element_located(self.locate(element)))
        else:
            wait.until(expected_conditions.visibility_of_element_located(element))
        self.element_log.info("waiting for element {} to be visible within {} seconds".format(element, timeout))

    def wait_till_stalenes(self, element, timeout):
        wait = WebDriverWait(self.driver, timeout)
        if isinstance(element, str):
            wait.until(expected_conditions.staleness_of(self.locate(element)))
        else:
            wait.until(expected_conditions.staleness_of(element))
        self.element_log.info("waiting for element {} to be stale within {} seconds".format(element, timeout))

    def wait_till_interact(self, element, timeout):
        wait = WebDriverWait(self.driver, timeout)
        if isinstance(element, str):
            wait.until(expected_conditions.element_to_be_clickable(self.locate(element)))
        else:
            wait.until(expected_conditions.element_to_be_clickable(element))
        self.element_log.info("waiting for element {} to be clickable within {} seconds".format(element, timeout))

    def wait_till_invisible(self, element, timeout):
        wait = WebDriverWait(self.driver, timeout)
        if isinstance(element, str):
            wait.until(expected_conditions.invisibility_of_element(self.locate(element)))
        else:
            wait.until(expected_conditions.invisibility_of_element(element))
        self.element_log.info("waiting for element {} to be invisible within {} seconds".format(element, timeout))

    def wait_till_presence(self, element, timeout):
        wait = WebDriverWait(self.driver, timeout)
        if isinstance(element, str):
            wait.until(expected_conditions.presence_of_element_located(self.locate(element)))
        else:
            wait.until(expected_conditions.presence_of_element_located(element))
        self.element_log.info("waiting for element {} to be invisible within {} seconds".format(element, timeout))

    def get_attribute(self, *element, attribute):
        if len(element) == 1 and isinstance(element[0], str):
            att_val = self.driver.find_element(*self.locate(element[0])).get_attribute(attribute)
        else:
            att_val = self.driver.find_element(*element).get_attribute(attribute)
        self.element_log.info("attribute {} of element {} is {}".format(attribute, element, att_val))
        return att_val

    def select_drop_down_by_index(self, *element, index):
        if len(element) == 1 and isinstance(element[0], str):
            select = Select(self.driver.find_element(*self.locate(element[0])))
        else:
            select = Select(self.driver.find_element(*element))
        select.select_by_index(index)
        self.element_log.info("selecting index {} from dropdown {}".format(index, element))

    def select_drop_down_by_value(self, *element, value):
        if len(element) == 1 and isinstance(element[0], str):
            select = Select(self.driver.find_element(*self.locate(element[0])))
        else:
            select = Select(self.driver.find_element(*element))
        select.select_by_value(value)
        self.element_log.info("selecting value {} from dropdown {}".format(value, element))

    def select_drop_down_by_text(self, *element, text):
        if len(element) == 1 and isinstance(element[0], str):
            select = Select(self.driver.find_element(*self.locate(element[0])))
        else:
            select = Select(self.driver.find_element(*element))
        select.select_by_visible_text(text)
        self.element_log.info("selecting text {} from dropdown {}".format(text, element))

    def deselect_drop_down_by_index(self, *element, index):
        if len(element) == 1 and isinstance(element[0], str):
            select = Select(self.driver.find_element(*self.locate(element[0])))
        else:
            select = Select(self.driver.find_element(*element))
        select.deselect_by_index(index)
        self.element_log.info("deselecting index {} from dropdown {}".format(index, element))

    def deselect_drop_down_by_value(self, *element, value):
        if len(element) == 1 and isinstance(element[0], str):
            select = Select(self.driver.find_element(*self.locate(element[0])))
        else:
            select = Select(self.driver.find_element(*element))
        select.deselect_by_value(value)
        self.element_log.info("deselecting value {} from dropdown {}".format(value, element))

    def deselect_drop_down_by_text(self, *element, text):
        if len(element) == 1 and isinstance(element[0], str):
            select = Select(self.driver.find_element(*self.locate(element[0])))
        else:
            select = Select(self.driver.find_element(*element))
        select.deselect_by_visible_text(text)
        self.element_log.info("deselecting text {} from dropdown {}".format(text, element))

    def right_click(self, *element):
        action = ActionChains(self.driver)
        if len(element) == 1 and isinstance(element[0], str):
            action.context_click(self.driver.find_element(*self.locate(element[0]))).perform()
        else:
            action.context_click(self.driver.find_element(*element)).perform()
        self.element_log.info("right clicking on element {}".format(element))

    def move_to_element(self, *element):
        action = ActionChains(self.driver)
        if len(element) == 1 and isinstance(element[0], str):
            action.move_to_element(self.driver.find_element(*self.locate(element[0])))
        else:
            action.move_to_element(self.driver.find_element(*element))
        self.element_log.info("right moving to element {}".format(element))

    def drag_and_drop(self, drag, drop):
        action = ActionChains(self.driver)
        action.drag_and_drop(self.driver.find_element(drag), self.driver.find_element(drop)).perform()
        self.element_log.info("dragging from {} dropping to {}".format(drag, drop))

    def is_displayed(self, *element):
        if len(element) == 1 and isinstance(element[0], str):
            is_displayed = self.driver.find_element(*self.locate(element[0])).is_displayed()
        else:
            is_displayed = self.driver.find_element(*element).is_displayed()
        self.element_log.info("is element {} displayed : {}".format(element, is_displayed))
        return is_displayed

    def is_selected(self, *element):
        if len(element) == 1 and isinstance(element[0], str):
            is_selected = self.driver.find_element(*self.locate(element[0])).is_selected()
        else:
            is_selected = self.driver.find_element(*element).is_selected()
        self.element_log.info("is element {} selected : {}".format(element, is_selected))
        return is_selected

    def is_enabled(self, *element):
        if len(element) == 1 and isinstance(element[0], str):
            is_enabled = self.driver.find_element(*self.locate(element[0])).is_enabled()
        else:
            is_enabled = self.driver.find_element(*element).is_enabled()
        self.element_log.info("is element {} enabled : {}".format(element, is_enabled))
        return is_enabled

    def scroll_to_element(self, *element):
        if len(element) == 1 and isinstance(element[0], str):
            self.driver.execute_script("arguments[0].scrollIntoView();",
                                       self.driver.find_element(*self.locate(element[0])))
        else:
            self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*element))

    def get_elements_count(self, *element):
        return len(self.driver.find_elements(*element))

    def locate(self, locator):
        using = locator.split(":::")[0]
        locator = locator.split(":::")[1]
        if using.lower() == "id":
            element = (By.ID, locator)
            return element
        elif using.lower() == "name":
            element = (By.NAME, locator)
            return element
        elif using.lower() == "class_name":
            element = (By.CLASS_NAME, locator)
            return element
        elif using.lower() == "tag_name":
            element = (By.TAG_NAME, locator)
            return element
        elif using.lower() == "link_text":
            element = (By.LINK_TEXT, locator)
            return element
        elif using.lower() == "partial_link_text":
            element = (By.PARTIAL_LINK_TEXT, locator)
            return element
        elif using.lower() == "css":
            element = (By.CSS_SELECTOR, locator)
            return element
        elif using.lower() == "xpath":
            element = (By.XPATH, locator)
            return element
        else:
            raise InvalidLocatorException("Not a valid locator: {}".format(using))

    def get_element(self, *element):
        return self.driver.find_element(*element)

    def get_elements(self, *element):
        return self.driver.find_elements(*element)

    def get_test_from_webelement(self,element):
        text = element.text
        self.element_log.info("text value of element {} is {}".format(element, text))
        return text