from selenium.webdriver.common.by import By
from lib.base_page import BasePage
from hamcrest import equal_to
from lib.assertions import assert_that


class RadioButton(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    select_txt = (By.XPATH, "//*[@class='text-success']")

    def click_on_selected_button(self, name: str, text):
        element = (By.XPATH, f"//*[@for='{name}Radio']")
        self.find_and_click(element)
        if name != "no":
            actual_result = self.find(self.select_txt, get_text=True)
            assert_that(actual_result, equal_to(text))
        else:
            actual_result = "Not clickable"
            assert_that(actual_result, equal_to(text))
