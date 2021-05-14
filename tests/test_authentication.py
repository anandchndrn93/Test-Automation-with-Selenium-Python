import pytest
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from utilities.actionUtil import ActionUtil
from utilities.commonUtil import CommonUtil
from utilities.waitUtil import WaitUtil


class TestAuthentication(BaseClass):

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.order(1)
    def test_login(self, getLoginData):
        home = HomePage(self.driver)
        wait = WaitUtil(self.driver)
        log = self.getlogger()
        log.info("verify login")
        home.getLoginLink().click()
        wait.waitforVisibilityofElement(home.loginPopUp)
        log.debug("login window opened")
        username = getLoginData.get("TestData", "email")
        password = getLoginData.get("TestData", "password")
        log.info("Loging in as user " + username)
        home.getUernameTextBox().clear()
        home.getUernameTextBox().send_keys(username)
        log.debug("Entered user name " + username)
        home.getPasswordTextBox().clear()
        home.getPasswordTextBox().send_keys(password)
        log.debug("entered password " + password)
        home.getLoginButton().click()
        wait.waitforVisibilityofElement(home.logOutLink)
        nameOfLoggedInUser = home.getLoggedInUserText().text
        assert username in nameOfLoggedInUser, "expected was " + username + " but got " + nameOfLoggedInUser
        log.debug("logged in username is visible in home page")

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.order(2)
    def test_logout(self, getLoginData):
        home = HomePage(self.driver)
        wait = WaitUtil(self.driver)
        log = self.getlogger()
        log.info("login")
        home.getLoginLink().click()
        wait.waitforVisibilityofElement(home.loginPopUp)
        log.debug("login window opened")
        username = getLoginData.get("TestData", "email")
        password = getLoginData.get("TestData", "password")
        log.info("Loging in as user " + username)
        home.getUernameTextBox().clear()
        home.getUernameTextBox().send_keys(username)
        log.debug("Entered user name " + username)
        home.getPasswordTextBox().clear()
        home.getPasswordTextBox().send_keys(password)
        log.debug("entered password " + password)
        home.getLoginButton().click()
        wait.waitforVisibilityofElement(home.logOutLink)
        log.info("loging out")
        home.getLogOutLink().click()
        log.info("logout link was clicked")
        wait.waitforVisibilityofElement(home.loginLink)
        assert not home.getUernameTextBox().is_displayed(), "user name is still present in home page"
        log.debug("logged out username is not visible in home page")
        log.debug("user was successfully logged out")

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.order(3)
    def test_invalid_user_login(self):
        username = "invalid_user@demo.com"
        password = "password"
        home = HomePage(self.driver)
        wait = WaitUtil(self.driver)
        action = ActionUtil(self.driver)
        log = self.getlogger()
        log.info("verify login with invalid user")
        wait.waitforVisibilityofElement(home.loginLink)
        home.getLoginLink().click()
        wait.waitforVisibilityofElement(home.loginPopUp)
        log.debug("login window opened")
        log.info("Loging in as user " + username)
        home.getUernameTextBox().clear()
        home.getUernameTextBox().send_keys(username)
        log.debug("Entered user name " + username)
        home.getPasswordTextBox().clear()
        home.getPasswordTextBox().send_keys(password)
        log.debug("entered password " + password)
        home.getLoginButton().click()
        alert = action.getAlert()
        alertText = alert.text
        log.debug("alert opened with text: " + alertText)
        assert alertText == "User does not exist.", "the alert text does not match expected"
        log.debug("the alert text matches expected")
        alert.accept()
        log.debug("alert accepted")
        home.getCloseLoginWindow().click()
        log.debug("login window was closed")

    @pytest.mark.regression
    @pytest.mark.order(4)
    def test_cancel_login(self, getLoginData):
        home = HomePage(self.driver)
        wait = WaitUtil(self.driver)
        log = self.getlogger()
        log.info("verify login")
        wait.waitforVisibilityofElement(home.loginLink)
        home.getLoginLink().click()
        wait.waitforVisibilityofElement(home.loginPopUp)
        log.debug("login window opened")
        username = getLoginData.get("TestData", "email")
        password = getLoginData.get("TestData", "password")
        log.info("Loging in as user " + username)
        home.getUernameTextBox().clear()
        home.getUernameTextBox().send_keys(username)
        log.debug("Entered user name " + username)
        home.getPasswordTextBox().clear()
        home.getPasswordTextBox().send_keys(password)
        log.debug("entered password " + password)
        home.getCloseLoginWindow().click()
        log.debug("login window was closed")
        wait.waitforVisibilityofElement(home.loginLink)
        assert not home.getUernameTextBox().is_displayed(), "user was logged in"
        log.debug("username is not visible in home page")
        log.debug("user was successfully  able to cancel login window")

    @pytest.fixture(params=[CommonUtil.readPropertyFile("./TestData/data.properties")])
    def getLoginData(self, request):
        return request.param
