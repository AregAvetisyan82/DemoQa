from selenium.webdriver.common.by import By
from lib.base_page import BasePage


class InteractionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    elements_list = ["Sortable", "Selectable", "Resizable", "Droppable", "Dragabble"]

    def go_to_selected_element(self, name: str):
        selected_page_number = self.elements_list.index(name)
        element = (By.ID, f'item-{selected_page_number}')
        self.select_element(element)
