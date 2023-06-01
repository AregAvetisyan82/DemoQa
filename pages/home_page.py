from selenium.webdriver.common.by import By
from lib.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    elements_list = ["", "Elements", "Forms", "Alerts, Frame & Windows", "Widgets", "Interactions",
                     "Book Store Application"]

    def go_to_selected_page(self, name: str):
        selected_page_number = self.elements_list.index(name)
        element = (By.XPATH, f'(//*[@xmlns="http://www.w3.org/2000/svg"])[{selected_page_number}]')
        self.scroll_to(self.find(element))
        self.find_and_click(element)
