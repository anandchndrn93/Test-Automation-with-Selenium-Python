import pytest

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from utilities.actionUtil import ActionUtil
from utilities.commonUtil import CommonUtil
from utilities.waitUtil import WaitUtil


class TestContact(BaseClass):
    @pytest.mark.regression
    def test_sendMessage(self, getContactData):
        home = HomePage(self.driver)
        wait = WaitUtil(self.driver)
        action = ActionUtil(self.driver)
        email = getContactData.get("TestData", "email")
        name = getContactData.get("TestData", "name")
        log = self.getlogger()
        home.getContactlink().click()
        log.info("accessing contact")
        wait.waitforVisibilityofElement(home.newMessageText)
        log.debug(" message window has opened")
        log.info("filling message details")
        home.getEmailTextBox().clear()
        home.getEmailTextBox().send_keys(email)
        log.debug("email " + email + " was entered")
        home.getNameTextbox().clear()
        home.getNameTextbox().send_keys(name)
        log.debug("name " + name + " was entered")
        home.getMessageTextbox().clear()
        home.getMessageTextbox().send_keys("Thanks for the DemoSite.")
        log.debug("message Thanks for the DemoSite was entered")
        home.getSendMessageButton().click()
        alert = action.getAlert()
        alertText = alert.text
        log.debug("alert opened with text: " + alertText)
        assert alertText == "Thanks for the message!!", "the alert text does not match expected"
        log.debug("the alert text matches expected")
        alert.accept()
        log.debug("alert accepted")

    @pytest.fixture(params=[CommonUtil.readPropertyFile("./TestData/data.properties")])
    def getContactData(self, request):
        return request.param
