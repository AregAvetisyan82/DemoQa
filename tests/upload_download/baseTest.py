import pytest
from testdata.testing_data import url


@pytest.mark.usefixtures("get_driver")
class BaseTest:

    def navigate_and_select_upload_button(self, file, path):
        self.base_page.go_to_page(url)
        self.home_page.go_to_selected_page("Elements")
        self.elements_page.go_to_selected_element("Upload and Download")
        self.upload_download_page.upload_file(file, path)

    def navigate_and_select_download_button(self, file: str):
        self.base_page.go_to_page(url)
        self.home_page.go_to_selected_page("Elements")
        self.elements_page.go_to_selected_element("Upload and Download")
        self.upload_download_page.download_file(file)
