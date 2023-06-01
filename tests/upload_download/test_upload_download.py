import pytest
from tests.upload_download.baseTest import BaseTest
from testdata.testing_data import FILE_UPLOAD, FILE_DOWNLOAD, UPLOAD_PATH


@pytest.mark.upload_download
class TestUploadDownload(BaseTest):
    def test_successful_upload_file(self):
        self.navigate_and_select_upload_button(FILE_UPLOAD, UPLOAD_PATH)

    def test_successful_download_file(self):
        self.navigate_and_select_download_button(FILE_DOWNLOAD)
