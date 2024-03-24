import pytest
from selenium.common.exceptions import StaleElementReferenceException
from utilities.common_util import CommonUtil


@pytest.mark.usefixtures("setup")
class TestPurchase:

    @pytest.mark.order(1)
    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.purchase
    def test_purchaseProduct(self, getTestData, context):
        context.home.open_login_window()
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
        context.home.enter_user_name(username)
        context.home.enter_password(password)
        context.home.click_login_button()
        context.home.get_user_name()
        context.home.open_product_category(category)
        context.home.open_product_page(productName)
        text = context.product.get_product_price(productName)
        price = text[:text.index("*")]
        context.product.add_product_to_cart()
        alertText = context.common.get_alert_text()
        assert alertText == "Product added.", "the alert text does not match expected"
        context.common.accept_alert()
        context.cart.navigate_to_cart()
        assert productName == context.cart.product_in_cart(), "The product in cart does not match actual product"
        priceNumberValue = price[1:-1]
        assert priceNumberValue == context.cart.get_product_price(), "the price of product in cart does not match actual product price"
        context.cart.place_order()
        context.cart.enter_name(name)
        context.cart.enter_country(country)
        context.cart.enter_city(city)
        context.cart.enter_card(card)
        context.cart.enter_month(month)
        context.cart.enter_year(year)
        context.cart.purchase_product()

    @pytest.mark.order(2)
    @pytest.mark.regression
    @pytest.mark.purchase
    def test_purchaseAllProductsInCategory(self, getTestData, context):
        context.home.open_login_window()
        username = getTestData.get("TestData", "email")
        password = getTestData.get("TestData", "password")
        category = getTestData.get("TestData", "productCategory")
        name = getTestData.get("TestData", "name")
        country = getTestData.get("TestData", "country")
        city = getTestData.get("TestData", "city")
        card = getTestData.get("TestData", "card")
        month = getTestData.get("TestData", "month")
        year = getTestData.get("TestData", "year")
        context.home.enter_user_name(username)
        context.home.enter_password(password)
        context.home.click_login_button()
        context.home.get_user_name()
        currentCatelogSize = context.home.get_product_count()
        context.home.open_product_category(category)
        CategoryCatelogSize = currentCatelogSize
        while currentCatelogSize == CategoryCatelogSize:
            CategoryCatelogSize = context.home.get_product_count()
            context.home.open_product_category(category)

        xpathList = []
        while True:
            try:
                xpathList = context.home.getAllProductLinks().copy()
                break
            except StaleElementReferenceException:
                pass

        for xpath in xpathList:
            product = context.home.navigate_to_product(xpath)
            priceText = context.product.get_product_price(product)
            price = priceText[:priceText.index("*")].strip()
            context.product.add_product_to_cart()
            alertText = context.common.get_alert_text()
            assert alertText == "Product added.", "the alert text does not match expected"
            context.common.accept_alert()
            context.home.navigate_to_home()
            context.home.open_product_category(category)
            while CategoryCatelogSize != context.home.get_product_count():
                context.home.open_product_category(category)
        context.cart.navigate_to_cart()
        recorderPrice = context.cart.get_total_price()
        assert context.cart.calculate_total_price() == float(recorderPrice), " The recorded Total Price is incorrect"
        context.cart.place_order()
        context.cart.enter_name(name)
        context.cart.enter_country(country)
        context.cart.enter_city(city)
        context.cart.enter_card(card)
        context.cart.enter_month(month)
        context.cart.enter_year(year)
        context.cart.purchase_product()

    @pytest.fixture(params=[CommonUtil.readPropertyFile("./TestData/data.properties")])
    def getTestData(self, request):
        return request.param
