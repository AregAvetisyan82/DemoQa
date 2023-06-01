import pytest
from testdata.testing_data import TEXT_RESULTS
from tests.checkbox.baseTest import BaseTest


@pytest.mark.checkbox
class TestCheckbox(BaseTest):
    def test_ckeckbox_all_flow(self):
        self.navigate_and_select_all_checkboxes(TEXT_RESULTS)
