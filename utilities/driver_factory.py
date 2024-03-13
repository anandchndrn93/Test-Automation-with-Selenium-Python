from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager


class DriverFactory:

    def __init__(self):
        self.driver = None

    def setup_driver(self, browser="chrome", headless=True):
        if browser == "firefox":
            options = Options()
            options.headless = headless
            self.driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
        elif browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--no-sandbox")
            if headless:
                options.headless = headless
                options.add_argument("window-size=1920,1080")
            self.driver = webdriver.Chrome(options=options, service=ChromService(ChromeDriverManager().install()))
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            options.add_argument("--no-sandbox")
            if headless:
                options.headless = headless
                options.add_argument("window-size=1920,1080")
            self.driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
        elif browser == "ie":
            options = webdriver.IeOptions()
            options.add_argument('--window-size=1920,1080')
            options.add_argument('--no-sandbox')
            self.driver = webdriver.Ie(options=options, service=IEService(IEDriverManager().install()))
        return self.driver
