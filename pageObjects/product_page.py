import time

from selenium.webdriver.common.by import By

from utilities.element_control import ElementControl
from utilities.page_control import PageControl


class ProductPage:
    addToCartLink = (By.XPATH, "//a[contains(@onclick,'addToCart')]")
    cartLink = (By.ID, "cartur")
    priceText = (By.XPATH, "//div[@id='tbodyid']/h3")
    homPageLink = (By.XPATH, "//a[contains(text(),'Home')]")
    product_name = "xpath::://h2[text()='{}']"

    def __init__(self, driver):
        self.driver = driver
        self.element_control = ElementControl(driver)
        self.page_control = PageControl(driver)

    def get_product_price(self, product):
        self.element_control.wait_till_visible(self.product_name.format(product), 5)
        return self.element_control.get_text(*self.priceText)

    def add_product_to_cart(self):
        self.element_control.wait_till_interact(self.addToCartLink, 5)
        self.element_control.click_element(*self.addToCartLink)