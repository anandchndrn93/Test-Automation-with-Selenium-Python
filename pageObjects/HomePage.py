import time

from selenium.webdriver.common.by import By


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

    def __init__(self, driver):
        self.driver = driver

    def getLoginLink(self):
        return self.driver.find_element(*HomePage.loginLink)

    def getUernameTextBox(self):
        time.sleep(1)
        return self.driver.find_element(*HomePage.usernameTextBox)

    def getPasswordTextBox(self):
        return self.driver.find_element(*HomePage.passwordTextBox)

    def getLoginButton(self):
        return self.driver.find_element(*HomePage.loginButton)

    def getLoggedInUserText(self):
        return self.driver.find_element(*HomePage.loggedInUserText)

    def getCloseLoginWindow(self):
        return self.driver.find_element(*HomePage.closeLoginButton)

    def getLogOutLink(self):
        return self.driver.find_element(*HomePage.logOutLink)

    def getContactlink(self):
        return self.driver.find_element(*HomePage.contactLink)

    def getNewMessage(self):
        return self.driver.find_element(*HomePage.newMessageText)

    def getEmailTextBox(self):
        return self.driver.find_element(*HomePage.emailTextbox)

    def getNameTextbox(self):
        return self.driver.find_element(*HomePage.nameTextbox)

    def getMessageTextbox(self):
        return self.driver.find_element(*HomePage.messageTextbox)

    def getSendMessageButton(self):
        return self.driver.find_element(*HomePage.sendMessageButton)

    def getProductCategoryLink(self, productCategory):
        xpath = "//a[contains(text(),'" + productCategory + "')]"
        return self.driver.find_element_by_xpath(xpath)

    def getProductTable(self):
        return self.driver.find_element(*HomePage.productTable)

    def getProductLink(self, product):
        xpath = "//a[contains(text(),'" + product + "')]"
        return self.driver.find_element_by_xpath(xpath)

    def getAllProductElements(self):
        return self.driver.find_elements(*HomePage.allProductLinks)

    def getAllProductLinks(self):
        productxpaths = []
        for element in self.getAllProductElements():
            productName = element.text
            product = "//a[contains(text(),'" + productName + "')]"
            productxpaths.append(product)
        return productxpaths

    def getElement(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def getCartLink(self):
        return self.driver.find_element(*HomePage.cartLink)