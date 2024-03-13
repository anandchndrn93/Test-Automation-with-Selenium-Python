import logging
import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from utilities.element_control import ElementControl


class HomePage:
    loginLink = (By.ID, "login2")
    usernameTextBox = (By.ID, "loginusername")
    passwordTextBox = (By.ID, "loginpassword")
    loginButton = (By.XPATH, "//button[@onclick='logIn()']")
    loggedInUserText = (By.ID, "nameofuser")
    logOutLink = (By.ID, "logout2")
    loginPopUp = (By.ID, "logInModalLabel")
    closeLoginButton = (By.XPATH, "//button[@onclick='logIn()']/preceding-sibling::button")
    contactLink = (By.XPATH, "//a[text()='Contact']")
    newMessageText = (By.ID, "exampleModalLabel")
    emailTextbox = (By.ID, "recipient-email")
    nameTextbox = (By.ID, "recipient-name")
    messageTextbox = (By.ID, "message-text")
    sendMessageButton = (By.XPATH, "//button[@onclick='send()']")
    productTable = (By.XPATH, "//div[@id='tbodyid']")
    allProductLinks = (By.XPATH, "//div[@id='tbodyid']//h4/a")
    cartLink = (By.ID, "cartur")
    product_category = "xpath::://a[contains(text(),'{}')]"
    product_link = "xpath::://a[contains(text(),'{}')]"
    log = logging.getLogger("demoblaze.home")
    homPageLink = (By.XPATH, "//a[contains(text(),'Home')]")

    def __init__(self, driver):
        self.driver = driver
        self.element_control = ElementControl(driver)

    def getAllProductLinks(self):
        productxpaths = []
        for element in self.element_control.get_elements(*self.allProductLinks):
            productName = element.text
            product = "//a[contains(text(),'" + productName + "')]"
            productxpaths.append(product)
        return productxpaths

    def open_login_window(self):
        self.element_control.click_element(*self.loginLink)
        self.element_control.wait_till_visible(self.loginPopUp, 10)

    def enter_user_name(self, user_name):
        self.element_control.clear_and_type(user_name, *self.usernameTextBox)

    def enter_password(self, password):
        self.element_control.clear_and_type(password, *self.passwordTextBox)

    def click_login_button(self):
        self.element_control.click_element(*self.loginButton)

    def get_user_name(self):
        self.element_control.wait_till_visible(self.logOutLink, 10)
        return self.element_control.get_text(*self.loggedInUserText)

    def log_out(self):
        self.element_control.wait_till_visible(self.logOutLink, 10)
        self.element_control.click_element(*self.logOutLink, )
        self.element_control.wait_till_visible(self.loginLink, 10)

    def is_username_displayed(self):
        return self.element_control.is_displayed(*self.loggedInUserText)

    def close_login_window(self):
        self.element_control.click_element(*self.closeLoginButton)
        self.element_control.wait_till_visible(self.loginLink, 10)

    def open_contact(self):
        self.element_control.click_element(*self.contactLink)
        self.element_control.wait_till_visible(self.newMessageText, 5)

    def enter_email(self, email):
        self.element_control.clear_and_type(email, *self.emailTextbox)

    def enter_name(self, name):
        self.element_control.clear_and_type(name, *self.nameTextbox)

    def enter_message(self, message):
        self.element_control.clear_and_type(message, *self.messageTextbox)

    def click_send_message_button(self):
        self.element_control.click_element(*self.sendMessageButton)

    def open_product_category(self, category):
        self.element_control.click_element(self.product_category.format(category))
        self.element_control.wait_till_visible(self.productTable, 5)

    def open_product_page(self, product):
        self.element_control.scroll_to_element(self.product_link.format(product))
        self.element_control.click_element(self.product_link.format(product))

    def get_product_count(self):
        return self.element_control.get_elements_count(*self.allProductLinks)

    def navigate_to_product(self, xpath):
        self.element_control.wait_till_presence((By.XPATH, xpath), 5)
        while True:
            try:
                element = (By.XPATH, xpath)
                self.element_control.scroll_to_element(*element)
                prodcutName = self.element_control.get_text(*element)
                self.element_control.click_element(*element)
                break
            except StaleElementReferenceException:
                self.log.info("some elements disappeared from dom.")
        self.log.info("opening product page for  " + prodcutName)
        return prodcutName

    def navigate_to_home(self):
        self.element_control.click_element(*self.homPageLink)
