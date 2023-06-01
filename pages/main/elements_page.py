from selenium.webdriver.common.by import By
from lib.base_page import BasePage


class ElementsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    elements_list = ["Text Box", "Check Box", "Radio Button", "Web Tables", "Buttons", "Links",
                     "Broken Links - Images", "Upload and Download", "Dynamic Properties"]

    def go_to_selected_element(self, name: str):
        selected_page_number = self.elements_list.index(name)
        element = (By.ID, f'item-{selected_page_number}')
        self.select_element(element)
