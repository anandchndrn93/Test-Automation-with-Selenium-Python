import re

import pytest
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

from pageObjects.CartPage import CartPage
from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage
from utilities.BaseClass import BaseClass
from utilities.actionUtil import ActionUtil
from utilities.commonUtil import CommonUtil
from utilities.waitUtil import WaitUtil


class TestPurchase(BaseClass):

    @pytest.mark.order(1)
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_purchaseProduct(self, getTestData):
        home = HomePage(self.driver)
        wait = WaitUtil(self.driver)
        action = ActionUtil(self.driver)
        product = ProductPage(self.driver)
        cart = CartPage(self.driver)
        log = self.getlogger()
        log.info("verify login")
        home.getLoginLink().click()
        wait.waitforVisibilityofElement(home.loginPopUp)
        log.debug("login window opened")
        username = getTestData.get("TestData", "email")
        password = getTestData.get("TestData", "password")
        category = getTestData.get("TestData", "productCategory")
        productName = getTestData.get("TestData", "productName")
        name = getTestData.get("TestData", "name")
        country = getTestData.get("TestData", "country")
        city = getTestData.get("TestData", "city")
        card = getTestData.get("TestData", "card")
        month = getTestData.get("TestData", "month")
        year = getTestData.get("TestData", "year")
        log.info("Loging in as user " + username)
        home.getUernameTextBox().clear()
        home.getUernameTextBox().send_keys(username)
        log.debug("Entered user name " + username)
        home.getPasswordTextBox().clear()
        home.getPasswordTextBox().send_keys(password)
        log.debug("entered password " + password)
        home.getLoginButton().click()
        wait.waitforVisibilityofElement(home.logOutLink)
        log.debug("user successfully logged in")
        home.getProductCategoryLink(category).click()
        log.debug("opening product category " + category)
        wait.waitforVisibilityofElement(home.productTable)
        action.scrollIntoView(home.getProductLink(productName))
        home.getProductLink(productName).click()
        log.debug("opening product page for  " + productName)
        wait.waitForElementToBeClickable(product.addToCartLink)
        text = product.getPriceText().text
        price = text[:text.index("*")]
        log.debug("Price of " + productName + " is " + price)
        product.getAddToCartLink().click()
        log.info("adding " + productName + " to the cart")
        alert = action.getAlert()
        alertText = alert.text
        log.debug("alert opened with text: " + alertText)
        assert alertText == "Product added.", "the alert text does not match expected"
        log.debug("the alert text matches expected")
        alert.accept()
        log.debug("alert accepted")
        log.debug(productName + " was added to the cart")
        log.info("Navigating to cart")
        product.getCartLink().click()
        wait.waitforVisibilityofElement(cart.addedProductTable)
        log.debug("cart was loaded")
        assert productName == cart.getAddedProductText().text, "The product in cart does not match actual product"
        log.debug("the product in cart is " + productName)
        priceNumberValue = price[1:-1]
        assert priceNumberValue == (cart.getAddedProductPriceText()[0]).text, "the price in cart does not match " \
                                                                              "product price "
        log.debug("the price in cart is {}".format(price))
        log.info("proceeding to pay")
        wait.waitforVisibilityofElement(cart.placeOrderButton)
        cart.getPlaceOrderButton().click()
        wait.waitforVisibilityofElement(cart.placeOrderText)
        log.debug("filling payment info")
        cart.getNameTextbox().clear()
        cart.getNameTextbox().send_keys(name)
        log.debug("name " + name + " entered")
        cart.getCountryTextbox().clear()
        cart.getCountryTextbox().send_keys(country)
        log.debug("country " + country + " entered")
        cart.getCityTextbox().clear()
        cart.getCityTextbox().send_keys(city)
        log.debug("city " + city + " entered")
        cart.getCardTextbox().clear()
        cart.getCardTextbox().send_keys(card)
        log.debug("card " + card + " entered")
        cart.getMonthTextbox().clear()
        cart.getMonthTextbox().send_keys(month)
        log.debug("month " + month + " entered")
        cart.getYearTextbox().clear()
        cart.getYearTextbox().send_keys(year)
        log.debug("month " + year + " entered")
        cart.getPurchaseButton().click()
        log.debug("purchasing product")
        wait.waitforVisibilityofElement(cart.thankText)
        log.debug("product purchase complete")
        cart.getOkButton().click()

    @pytest.mark.order(2)
    @pytest.mark.regression
    def test_purchaseAllProductsInCategory(self, getTestData):
        home = HomePage(self.driver)
        wait = WaitUtil(self.driver)
        action = ActionUtil(self.driver)
        product = ProductPage(self.driver)
        cart = CartPage(self.driver)
        log = self.getlogger()
        log.info("verify login")
        home.getLoginLink().click()
        wait.waitforVisibilityofElement(home.loginPopUp)
        log.debug("login window opened")
        username = getTestData.get("TestData", "email")
        password = getTestData.get("TestData", "password")
        category = getTestData.get("TestData", "productCategory")
        name = getTestData.get("TestData", "name")
        country = getTestData.get("TestData", "country")
        city = getTestData.get("TestData", "city")
        card = getTestData.get("TestData", "card")
        month = getTestData.get("TestData", "month")
        year = getTestData.get("TestData", "year")
        log.info("Loging in as user " + username)
        home.getUernameTextBox().clear()
        home.getUernameTextBox().send_keys(username)
        log.debug("Entered user name " + username)
        home.getPasswordTextBox().clear()
        home.getPasswordTextBox().send_keys(password)
        log.debug("entered password " + password)
        home.getLoginButton().click()
        wait.waitforVisibilityofElement(home.logOutLink)
        log.debug("user successfully logged in")
        currentCatelogSize = len(home.getAllProductElements())
        home.getProductCategoryLink(category).click()
        log.debug("opening product category " + category)
        wait.waitforVisibilityofElement(home.productTable)
        CategoryCatelogSize = currentCatelogSize
        while currentCatelogSize == CategoryCatelogSize:
            CategoryCatelogSize = len(home.getAllProductElements())
            home.getProductCategoryLink(category).click()
            wait.waitforVisibilityofElement(home.productTable)

        xpathList = []
        while True:
            try:
                xpathList = home.getAllProductLinks().copy()
                break
            except StaleElementReferenceException:
                log.debug("some elements disappeared from dom.")

        for xpath in xpathList:
            wait.waitForElementToBePresent((By.XPATH, xpath))
            while True:
                try:
                    element = home.getElement(xpath)
                    action.scrollIntoView(element)
                    prodcutName = element.text
                    element.click()
                    break
                except StaleElementReferenceException:
                    log.debug("some elements disappeared from dom.")
            log.debug("opening product page for  " + prodcutName)
            wait.waitforVisibilityofElement(product.addToCartLink)
            priceText = product.getPriceText().text
            price = priceText[:priceText.index("*")].strip()
            log.debug("Price of " + prodcutName + " is " + price)
            product.getAddToCartLink().click()
            log.info("adding " + prodcutName + " to the cart")
            alert = action.getAlert()
            addedToCartText = alert.text
            log.debug("alert opened with text: " + addedToCartText)
            assert addedToCartText == "Product added.", "the alert text does not match expected"
            log.debug("the alert text matches expected")
            alert.accept()
            log.debug("alert accepted")
            log.debug(prodcutName + " was added to the cart")
            product.getHomePageLink().click()
            home.getProductCategoryLink(category).click()
            log.debug("opening product category " + category)
            wait.waitforVisibilityofElement(home.productTable)
            while CategoryCatelogSize != len(home.getAllProductElements()):
                home.getProductCategoryLink(category).click()
                wait.waitforVisibilityofElement(home.productTable)
        log.debug("opening cart")
        home.getCartLink().click()
        wait.waitforVisibilityofElement(cart.addedProductTable)
        log.debug("cart was loaded")
        wait.waitforVisibilityofElement(cart.totalPriceText)
        recorderPrice = cart.getTotalPriceText().text
        log.debug("Total Price is {}".format(recorderPrice))
        TotalPrice = 0
        for element in cart.getAddedProductPriceText():
            TotalPrice += float(element.text)
        assert TotalPrice == float(recorderPrice), " The recorded Total Price is incorrect"
        log.info("proceeding to pay")
        wait.waitforVisibilityofElement(cart.placeOrderButton)
        cart.getPlaceOrderButton().click()
        wait.waitforVisibilityofElement(cart.placeOrderText)
        log.debug("filling payment info")
        cart.getNameTextbox().clear()
        cart.getNameTextbox().send_keys(name)
        log.debug("name " + name + " entered")
        cart.getCountryTextbox().clear()
        cart.getCountryTextbox().send_keys(country)
        log.debug("country " + country + " entered")
        cart.getCityTextbox().clear()
        cart.getCityTextbox().send_keys(city)
        log.debug("city " + city + " entered")
        cart.getCardTextbox().clear()
        cart.getCardTextbox().send_keys(card)
        log.debug("card " + card + " entered")
        cart.getMonthTextbox().clear()
        cart.getMonthTextbox().send_keys(month)
        log.debug("month " + month + " entered")
        cart.getYearTextbox().clear()
        cart.getYearTextbox().send_keys(year)
        log.debug("month " + year + " entered")
        cart.getPurchaseButton().click()
        log.debug("purchasing product")
        wait.waitforVisibilityofElement(cart.thankText)
        log.debug("product purchase complete")
        cart.getOkButton().click()

    @pytest.fixture(params=[CommonUtil.readPropertyFile("./TestData/data.properties")])
    def getTestData(self, request):
        return request.param
