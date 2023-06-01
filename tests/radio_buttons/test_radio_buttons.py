import pytest
from tests.radio_buttons.baseTest import BaseTest


@pytest.mark.radio
class TestRadioButtons(BaseTest):
    @pytest.mark.parametrize("name, result", [("yes", "Yes"), ("impressive", "Impressive"), ("no", "Not clickable")])
    def test_radio_buttons(self, name, result):
        self.navigate_and_select_yes_radio_button(name, result)
