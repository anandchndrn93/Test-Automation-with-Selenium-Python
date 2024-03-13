from utilities.page_control import PageControl
from utilities.element_control import ElementControl


class CommonPage:

    def __init__(self, driver):
        self.driver = driver
        self.page_control = PageControl(driver)
        self.element_control = ElementControl(driver)

    def get_alert_text(self):
        return self.page_control.get_alert_text(5)

    def accept_alert(self):
        self.page_control.accept_alert(5)
        self.page_control.wait_till_alert_not_present(2)

    def wait_for(self, time_out):
        self.element_control.wait_for(time_out)
