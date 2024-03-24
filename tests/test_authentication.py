import pytest
from utilities.common_util import CommonUtil


@pytest.mark.usefixtures("setup")
class TestAuthentication:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.auth
    @pytest.mark.order(1)
    def test_login(self, getLoginData, context):
        context.home.open_login_window()
        username = getLoginData.get("TestData", "email")
        password = getLoginData.get("TestData", "password")
        context.home.enter_user_name(username)
        context.home.enter_password(password)
        context.home.click_login_button()
        name_of_logged_in_user = context.home.get_user_name()
        assert username in name_of_logged_in_user, "expected was " + username + " but got " + name_of_logged_in_user

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.auth
    @pytest.mark.order(2)
    def test_logout(self, getLoginData, context):
        context.home.open_login_window()
        username = getLoginData.get("TestData", "email")
        password = getLoginData.get("TestData", "password")
        context.home.enter_user_name(username)
        context.home.enter_password(password)
        context.home.click_login_button()
        context.home.log_out()
        assert not context.home.is_username_displayed(), "user name is still present in home page"

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.auth
    @pytest.mark.order(3)
    def test_invalid_user_login(self, context):
        username = "invalid_user@demo.com"
        password = "password"
        context.home.open_login_window()
        context.home.enter_user_name(username)
        context.home.enter_password(password)
        context.home.click_login_button()
        alertText = context.common.get_alert_text()
        assert alertText == "User does not exist.", "the alert text does not match expected"
        context.common.accept_alert()
        context.home.close_login_window()

    @pytest.mark.regression
    @pytest.mark.auth
    @pytest.mark.order(4)
    def test_cancel_login(self, getLoginData, context):
        context.home.open_login_window()
        username = getLoginData.get("TestData", "email")
        password = getLoginData.get("TestData", "password")
        context.home.enter_user_name(username)
        context.home.enter_password(password)
        context.home.close_login_window()
        assert not context.home.is_username_displayed(), "user was logged in"

    @pytest.fixture(params=[CommonUtil.readPropertyFile("./TestData/data.properties")])
    def getLoginData(self, request):
        return request.param