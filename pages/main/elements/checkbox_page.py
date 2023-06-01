from selenium.webdriver.common.by import By
from lib.base_page import BasePage
from hamcrest import equal_to
from lib.assertions import assert_that


class CheckboxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    expand_all_btn = (By.XPATH, "//*[@aria-label='Expand all']")
    collapse_all_btn = (By.XPATH, "//*[@aria-label='Collapse all']")

    name_list = ["home", "desktop", "notes", "commands", "documents", "workspace", "react", "angular", "veu",
                 "office", "public", "private", "classified", "general", "downloads", "wordFile", "excelFile"]

    result_text = (By.ID, "result")

    def select_all_checkbox_selection_and_assert_result(self, text: str):
        self.find_and_click(self.expand_all_btn)
        self.find_and_click(self.collapse_all_btn)
        for i in range(1, 7):
            element = (By.XPATH, f'(//*[@aria-label="Toggle"])[{i}]')
            self.find_and_click(element)
        for i in self.name_list:
            element = (By.XPATH, f"//label[@for='tree-node-{i}']")
            self.find_and_click(element)
        selected_items = self.find(self.result_text, get_text=True)
        assert_that(selected_items, equal_to(text))
