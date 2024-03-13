import logging

from selenium.common import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PageControl:
    page_log = logging.getLogger("demoblaze.page")

    def __init__(self, driver):
        self.driver = driver

    def load_url(self, url):
        self.driver.get(url)
        self.page_log.info("fetched page :" + url)

    def maximize_window(self):
        self.driver.maximize_window()

    def get_url(self):
        url = self.driver.current_url
        self.page_log.info("the current url is : " + url)
        return url

    def wait_for_alert(self, time_out):
        wait = WebDriverWait(self.driver, time_out)
        self.page_log.info("waiting for alert to be preset")
        wait.until(expected_conditions.alert_is_present())

    def accept_alert(self, time_out):
        self.wait_for_alert(time_out)
        Alert(self.driver).accept()

    def decline_alert(self, time_out):
        self.wait_for_alert(time_out)
        Alert(self.driver).dismiss()

    def get_alert_text(self, time_out):
        self.wait_for_alert(time_out)
        text = Alert(self.driver).text
        self.page_log.info("Alert text is : " + text)
        return text

    def get_title(self):
        title = self.driver.title
        self.page_log.info("title is : " + title)
        return title

    def close_browser(self):
        self.driver.close()
        self.page_log.info("current browser window is closed")

    def quit_browser(self):
        self.driver.quit()
        self.page_log.info("browser is closed")

    def refresh_page(self):
        self.driver.refresh()
        self.page_log.info("current page is refreshed")

    def implicit_wait(self, time_out):
        self.driver.implicitly_wait(time_out)
        self.page_log.info("implicit wait is set to " + time_out + " seconds")

    def remove_implicit_wait(self):
        self.driver.implicitly_wait(0)
        self.page_log.info("implicit wait is removed")

    def page_load_timeout(self, time_out):
        self.driver.set_page_load_timeout(time_out)
        self.page_log.info("page load timeout is set to " + time_out + " seconds")

    def navigate_to_child_window(self):
        handles = self.driver.window_handles
        last_window = handles[-1]
        self.driver.switch_to.window(last_window)
        self.page_log.info("switched to last window")

    def switch_to_window(self, window_number):
        handles = self.driver.window_handles
        n_window = handles[window_number]
        self.driver.switch_to.window(n_window)
        self.page_log.info("switched to window " + window_number)

    def scroll_to_bottom_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.page_log.info("scrolled to bottom page")

    def wait_till_alert_not_present(self, time_out):
        try:
            WebDriverWait(self.driver, time_out).until(expected_conditions.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            self.page_log.info("alert Exists in page")
        except TimeoutException:
            self.page_log.info("alert does not Exist in page")