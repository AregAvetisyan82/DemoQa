import pytest
from tests.textbox.baseTest import BaseTest
from testdata.testing_data import FULL_NAME, EMAIL, CURRENT_ADDRESS, PERMANENT_ADDRESS, TEXT_OUTPUT, \
    EXPECTED_RESULT, INVALID_EMAIL


@pytest.mark.textbox
class TestTextBox(BaseTest):
    def test_successful_full_name_input(self):
        self.navigate_and_enter_data_in_textbox(FULL_NAME, TEXT_OUTPUT[0])

    def test_successful_email_input(self):
        self.navigate_and_enter_data_in_textbox(EMAIL, TEXT_OUTPUT[1])

    def test_successful_curr_addr_input(self):
        self.navigate_and_enter_data_in_textbox(CURRENT_ADDRESS, TEXT_OUTPUT[2])

    def test_successful_perm_addr_input(self):
        self.navigate_and_enter_data_in_textbox(PERMANENT_ADDRESS, TEXT_OUTPUT[3])

    def test_successful_all_inputs(self):
        self.navigate_and_enter_data_in_textbox(FULL_NAME, EMAIL, CURRENT_ADDRESS, PERMANENT_ADDRESS, EXPECTED_RESULT)

    @pytest.mark.negative
    @pytest.mark.parametrize("email", INVALID_EMAIL)
    def test_invalid_email_format_input(self, email):
        self.navigate_and_enter_data_in_textbox(email=email, expected_result="")
