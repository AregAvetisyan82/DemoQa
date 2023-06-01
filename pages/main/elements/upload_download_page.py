from selenium.webdriver.common.by import By
from lib.base_page import BasePage
from hamcrest import equal_to
from lib.assertions import assert_that


class UploadDownloadPage(BasePage):
    select_file_btn = (By.XPATH, '//*[@id="uploadFile"]')
    uploaded_file_path = (By.ID, "uploadedFilePath")
    download_btn = (By.ID, "downloadButton")

    def upload_file(self, file: str, path: str):
        file_to_upload = self.get_file_in_temp_folder(file)
        self.find_and_send_keys(self.select_file_btn, file_to_upload)
        selected_text = self.find(self.uploaded_file_path, get_text=True)
        assert_that(selected_text, equal_to(path))

    def download_file(self, file):
        self.find_and_click(self.download_btn)
        actual_result = self.file_in_downloads(file)
        assert_that(actual_result, equal_to(True))
