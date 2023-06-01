import pytest
from selenium import webdriver
from selenium.webdriver.safari.options import Options as Option
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pretty_debug import info_light_blue
from testdata.testing_data import browser
from lib.base_page import BasePage
from pages.home_page import HomePage
from pages.main.alerts_page import AlertsPage
from pages.main.books_page import BooksPage
from pages.main.elements_page import ElementsPage
from pages.main.forms_page import FormsPage
from pages.main.interactions_page import InteractionsPage
from pages.main.widgets_page import WidgetsPage
from pages.main.elements.checkbox_page import CheckboxPage
from pages.main.elements.radio_button_page import RadioButton
from pages.main.elements.textbox_page import TextPage
from pages.main.elements.upload_download_page import UploadDownloadPage

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=browser)


@pytest.fixture(scope="session", autouse=True)
def get_browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def get_driver(request, get_browser):
    global driver
    if get_browser == "chrome":
        options = Options()
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("-- disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        prefs = {'download.default_directory': '/Users/areg.avetisyan/Downloads',
                 "download.prompt_for_download": False,
                 "download.directory_upgrade": True,
                 "safebrowsing_for_trusted_sources_enabled": False,
                 "safebrowsing.enabled": False,
                 "profile.default_content_setting_values.notifications": 1, "block-new-web-contents": False}
        options.add_experimental_option('prefs', prefs)
        options.add_experimental_option('excludeSwitches', ['load-extension', 'enable-automation'])
        driver = webdriver.Chrome(options=options)
        driver.execute_script("window.alert = function() {};")
    elif get_browser == "edge":
        driver = webdriver.Edge()
    elif get_browser == "firefox":
        driver = webdriver.Firefox()
    elif get_browser == "safari":
        options = Option()
        driver = webdriver.Safari(options=options)
    elif get_browser == "headless":
        options = Options()
        options.add_argument("--headless")
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("-- disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        prefs = {'download.default_directory': '/Users/areg.avetisyan/Downloads',
                 "download.prompt_for_download": False,
                 "download.directory_upgrade": True,
                 "safebrowsing_for_trusted_sources_enabled": False,
                 "safebrowsing.enabled": False,
                 "profile.default_content_setting_values.notifications": 1, "block-new-web-contents": False}
        options.add_experimental_option('prefs', prefs)
        options.add_experimental_option('excludeSwitches', ['load-extension', 'enable-automation'])
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.execute_script("window.alert = function() {};")
    else:
        raise ValueError("Invalid driver name")
    driver.implicitly_wait(10)
    request.cls.base_page = BasePage(driver)
    request.cls.home_page = HomePage(driver)
    request.cls.alerts_page = AlertsPage(driver)
    request.cls.books_page = BooksPage(driver)
    request.cls.elements_page = ElementsPage(driver)
    request.cls.forms_page = FormsPage(driver)
    request.cls.interactions_page = InteractionsPage(driver)
    request.cls.widgets_page = WidgetsPage(driver)
    request.cls.checkbox_page = CheckboxPage(driver)
    request.cls.radio_button_page = RadioButton(driver)
    request.cls.textbox_page = TextPage(driver)
    request.cls.upload_download_page = UploadDownloadPage(driver)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def log_test_name(request):
    info_light_blue(f"\nTest '{request.node.nodeid}' STARTED\n")

    def fin():
        info_light_blue(f"\n Test '{request.node.nodeid}' COMPLETED\n")
    request.addfinalizer(fin)
