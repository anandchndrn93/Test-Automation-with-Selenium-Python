import time

from selenium.webdriver.common.by import By


class CartPage:
    addedProductTable = (By.XPATH, "//tbody[@id='tbodyid']")
    addedProductText = (By.XPATH, "//tbody[@id='tbodyid']/tr/td[2]")
    addedProductPriceText = (By.XPATH, "//tbody[@id='tbodyid']/tr/td[3]")
    placeOrderButton = (By.XPATH, "//h3[@id='totalp']/ancestor::div/button")
    placeOrderText = (By.ID, "orderModalLabel")
    nameTextbox = (By.ID, "name")
    countryTextbox = (By.ID, "country")
    cityTextbox = (By.ID, "city")
    cardTextbox = (By.ID, "card")
    monthTextbox = (By.ID, "month")
    yearTextbox = (By.ID, "year")
    purchaseButton = (By.XPATH, "//button[@onclick='purchaseOrder()']")
    thankText = (By.XPATH, "//h2[contains(text(),'Thank you')]")
    okButton = (By.XPATH, "//button[contains(text(),'OK')]")
    totalPriceText = (By.ID, "totalp")

    def __init__(self, driver):
        self.driver = driver

    def getAddedProductTable(self):
        return self.driver.find_element(*CartPage.addedProductTable)

    def getAddedProductText(self):
        time.sleep(3)
        return self.driver.find_element(*CartPage.addedProductText)

    def getAddedProductPriceText(self):
        return self.driver.find_elements(*CartPage.addedProductPriceText)

    def getPlaceOrderButton(self):
        return self.driver.find_element(*CartPage.placeOrderButton)

    def getPlaceOrderText(self):
        return self.driver.find_element(*CartPage.placeOrderText)

    def getNameTextbox(self):
        return self.driver.find_element(*CartPage.nameTextbox)

    def getCountryTextbox(self):
        return self.driver.find_element(*CartPage.countryTextbox)

    def getCityTextbox(self):
        return self.driver.find_element(*CartPage.cityTextbox)

    def getCardTextbox(self):
        return self.driver.find_element(*CartPage.cardTextbox)

    def getMonthTextbox(self):
        return self.driver.find_element(*CartPage.monthTextbox)

    def getYearTextbox(self):
        return self.driver.find_element(*CartPage.yearTextbox)

    def getPurchaseButton(self):
        return self.driver.find_element(*CartPage.purchaseButton)

    def getThankText(self):
        return self.driver.find_element(*CartPage.thankText)

    def getOkButton(self):
        return self.driver.find_element(*CartPage.okButton)

    def getTotalPriceText(self):
        return self.driver.find_element(*CartPage.totalPriceText)