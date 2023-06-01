import pytest
from testdata.testing_data import url


@pytest.mark.usefixtures("get_driver")
class BaseTest:

    def navigate_and_select_all_checkboxes(self, text):
        self.base_page.go_to_page(url)
        self.home_page.go_to_selected_page("Elements")
        self.elements_page.go_to_selected_element("Check Box")
        self.checkbox_page.select_all_checkbox_selection_and_assert_result(text)
