import time

from selenium.webdriver.common.by import By


class ProductPage:
    addToCartLink = (By.XPATH, "//a[contains(@onclick,'addToCart')]")
    cartLink = (By.ID, "cartur")
    priceText = (By.XPATH, "//div[@id='tbodyid']/h3")
    homPageLink = (By.XPATH, "//a[contains(text(),'Home')]")

    def __init__(self, driver):
        self.driver = driver

    def getAddToCartLink(self):
        return self.driver.find_element(*ProductPage.addToCartLink)

    def getCartLink(self):
        return self.driver.find_element(*ProductPage.cartLink)

    def getPriceText(self):
        return self.driver.find_element(*ProductPage.priceText)

    def getHomePageLink(self):
        return self.driver.find_element(*ProductPage.homPageLink)
