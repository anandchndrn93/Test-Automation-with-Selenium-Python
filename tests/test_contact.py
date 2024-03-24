import pytest

from utilities.common_util import CommonUtil


@pytest.mark.usefixtures("setup")
class TestContact:
    @pytest.mark.regression
    @pytest.mark.contact
    def test_sendMessage(self, getContactData, context):
        email = getContactData.get("TestData", "email")
        name = getContactData.get("TestData", "name")
        context.home.open_contact()
        context.home.enter_email(email)
        context.home.enter_name(name)
        context.home.enter_message("Thanks for the DemoSite.")
        context.home.click_send_message_button()
        alertText = context.common.get_alert_text()
        assert alertText == "Thanks for the message!!", "the alert text does not match expected"
        context.common.accept_alert()

    @pytest.fixture(params=[CommonUtil.readPropertyFile("./TestData/data.properties")])
    def getContactData(self, request):
        return request.param
