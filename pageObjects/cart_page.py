import time

from selenium.webdriver.common.by import By

from utilities.element_control import ElementControl


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
    cartLink = (By.ID, "cartur")

    def __init__(self, driver):
        self.driver = driver
        self.element_control = ElementControl(driver)

    def navigate_to_cart(self):
        self.element_control.click_element(*self.cartLink)
        self.element_control.wait_till_visible(self.addedProductTable, 5)

    def product_in_cart(self):
        time.sleep(3)
        return self.element_control.get_text(*self.addedProductText)

    def get_product_price(self):
        return self.element_control.get_text(*self.addedProductPriceText)

    def place_order(self):
        self.element_control.wait_till_interact(self.placeOrderButton, 5)
        self.element_control.click_element(*self.placeOrderButton)
        self.element_control.wait_till_visible(self.placeOrderText, 5)

    def enter_name(self, name):
        self.element_control.clear_and_type(name, *self.nameTextbox)

    def enter_country(self, country):
        self.element_control.clear_and_type(country, *self.countryTextbox)

    def enter_city(self, city):
        self.element_control.clear_and_type(city, *self.cityTextbox)

    def enter_card(self, card):
        self.element_control.clear_and_type(card, *self.cardTextbox)

    def enter_month(self, month):
        self.element_control.clear_and_type(month, *self.monthTextbox)

    def enter_year(self, year):
        self.element_control.clear_and_type(year, *self.yearTextbox)

    def purchase_product(self):
        self.element_control.click_element(*self.purchaseButton)
        self.element_control.wait_till_visible(self.thankText, 5)
        self.element_control.wait_till_interact(self.okButton, 5)
        self.element_control.click_element(*self.okButton)

    def get_total_price(self):
        self.element_control.wait_till_visible(self.totalPriceText, 5)
        return self.element_control.get_text(*self.totalPriceText)

    def calculate_total_price(self):
        total_price = 0
        for element in self.element_control.get_elements(*self.addedProductPriceText):
            print(element)
            total_price += float(self.element_control.get_test_from_webelement(element))
        return total_price
