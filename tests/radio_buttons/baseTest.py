import pytest
from testdata.testing_data import url


@pytest.mark.usefixtures("get_driver")
class BaseTest:

    def navigate_and_select_yes_radio_button(self, name, text):
        self.base_page.go_to_page(url)
        self.home_page.go_to_selected_page("Elements")
        self.elements_page.go_to_selected_element("Radio Button")
        self.radio_button_page.click_on_selected_button(name, text)
