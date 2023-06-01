from selenium.webdriver.common.by import By
from lib.base_page import BasePage
from hamcrest import equal_to
from lib.assertions import assert_that


class TextPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    full_name_inp = (By.ID, 'userName')
    email_inp = (By.ID, 'userEmail')
    curr_address_tbx = (By.ID, 'currentAddress')
    perm_address_tbx = (By.ID, 'permanentAddress')
    submit_btn = (By.ID, 'submit')
    total_out = (By.ID, 'output')

    def complete_textbox(self, full_name, email, curr_adr, perm_adr, expected_result):
        self.find_and_send_keys(self.full_name_inp, full_name)
        self.find_and_send_keys(self.email_inp, email)
        self.find_and_send_keys(self.curr_address_tbx, curr_adr)
        self.find_and_send_keys(self.perm_address_tbx, perm_adr)
        self.select_element(self.submit_btn)
        selected_text = self.find(self.total_out, get_text=True)
        assert_that(selected_text, equal_to(expected_result))
