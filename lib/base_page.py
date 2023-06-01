from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from os import path, remove
import time
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 20)

    def go_to_page(self, url, new_window=False):
        if new_window:
            self.driver.execute_script(f"window.open('{url}');")
        else:
            self.driver.get(url)
            self.driver.maximize_window()

    def find(self, loc, timeout=10, get_text=False, get_attribute=False):
        elem = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(loc))
        if get_text:
            return elem.text
        elif get_attribute:
            return elem.get_attribute(get_attribute)
        return elem

    def find_and_click(self, loc, timeout=10):
        elem = self.find(loc, timeout)
        elem.click()

    def find_and_send_keys(self, loc, inp_text, timeout=10):
        elem = self.find(loc, timeout)
        elem.send_keys(inp_text)

    def find_and_clear(self, loc, timeout=10):
        elem = self.find(loc, timeout)
        elem.send_keys(Keys.BACKSPACE*100)

    def switch_window(self, window_id=0):
        self.driver.switch_to.window(self.driver.window_handles[window_id])

    def switch_to_alert(self):
        return self.driver.switch_to.alert

    def refresh_page(self):
        self.driver.refresh()

    def focus_on_element(self, element):
        self.actions.move_to_element(element).perform()

    def focus_and_click(self, element):
        self.actions.move_to_element(element).click().perform()

    # def assert_result(self, actual_result, expected_result):
    #     try:
    #         assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'."
    #     except AssertionError as ex:
    #         print(ex)

    def assert_result(self, actual_result, expected_result):
        assert actual_result == expected_result

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def is_displayed(self, element):
        element.is_displayed()

    def is_clickable(self, loc):
        elem = self.find(loc)
        elem.is_clickable()

    def is_selected(self, element):
        element.is_selected()
        return True

    def select_element(self, loc):
        element = self.find(loc)
        self.scroll_to(element)
        self.focus_and_click(element)

    def get_file_in_temp_folder(self, FName):
        return path.join(path.dirname(path.dirname(path.realpath(__file__))), 'testdata/' + FName)

    # /Users/areg.avetisyan/Downloads/ - replace with your "Downloads" directory path
    def file_in_downloads(self, file_name):
        while not path.exists(f"/Users/areg.avetisyan/Downloads/{file_name}"):
            time.sleep(10)
        if path.isfile(f"/Users/areg.avetisyan/Downloads/{file_name}"):
            remove(f"/Users/areg.avetisyan/Downloads/{file_name}")
            return True
        else:
            raise ValueError("%s isn't a file!" % "/Users/areg.avetisyan/Downloads/")

    def back(self):
        self.driver.back()

    # def find_upload(self, loc, timeout=10, get_text=False, get_attribute=False):
    #     elem = WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(loc))
    #     if get_text:
    #         return elem.text
    #     elif get_attribute:
    #         return elem.get_attribute(get_attribute)
    #
    # def find_upload_and_send_keys(self, loc, inp_text, timeout=10):
    #     elem = self.find_upload(loc, timeout)
    #     elem.send_keys(inp_text)
