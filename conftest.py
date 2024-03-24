import logging

import pytest

from configs.constants import Constants
from pageObjects.cart_page import CartPage
from pageObjects.common_page import CommonPage
from pageObjects.home_page import HomePage
from pageObjects.product_page import ProductPage
from utilities.driver_factory import DriverFactory
from utilities.page_control import PageControl

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--headless", action="store", default=False
    )


@pytest.fixture()
def setup(request, context):
    global driver
    driver_manager = DriverFactory()
    driver = driver_manager.setup_driver(request.config.getoption("headless"), request.config.getoption("browser_name"))
    page_control = PageControl(driver)
    page_control.maximize_window()
    page_control.load_url(Constants.DEMO_URL)
    context.driver = driver
    context.home = HomePage(driver)
    context.product = ProductPage(driver)
    context.cart = CartPage(driver)
    context.common = CommonPage(driver)
    yield
    driver.close()


@pytest.fixture
def context(request):
    class Context(object):
        pass

    return Context()


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    logger = logging.getLogger("demoblaze")
    logger.setLevel(logging.DEBUG)
    # create file handler to log messages to file
    file_handler = logging.FileHandler(r"./demoblaze.log", mode='w')
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    # create console handler to log to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_").split(".py_")[1] + ".png"
            _capture_screenshot('results/screent_shots/' + file_name)
            if file_name:
                actual_file = 'screent_shots/' + file_name
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % actual_file
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.save_screenshot(name)
