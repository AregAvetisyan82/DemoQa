from selenium.webdriver.common.by import By
from lib.base_page import BasePage


class FormsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    practice_form_btn = (By.ID, "item-0")

    def go_to_selected_element_practice_form(self):
        self.select_element(self.practice_form_btn)
