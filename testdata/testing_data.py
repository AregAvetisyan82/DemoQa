browser = "chrome"
url = "https://demoqa.com/"

FULL_NAME = "Test Testsyan"
EMAIL = "test.testyan@testing.am"
CURRENT_ADDRESS = "12 Apt, 34 Bld, Testovyan Str., Testvan, TEST"
PERMANENT_ADDRESS = "01AB Testing Street, TEST, TESTING"

TEXT_OUTPUT = [f"Name:{FULL_NAME}", f"Email:{EMAIL}", f"Current Address :{CURRENT_ADDRESS}",
               f"Permananet Address :{PERMANENT_ADDRESS}"]
EXPECTED_RESULT = f"{TEXT_OUTPUT[0]}\n{TEXT_OUTPUT[1]}\n{TEXT_OUTPUT[2]}\n{TEXT_OUTPUT[3]}"

INVALID_EMAIL = ["example",
                 "#@%^%#$@#$@#.com",
                 "@example.com",
                 "Joe Smith <email@example.com>",
                 "email.example.com",
                 ".email@example.com",
                 "email.email+1@example.com"]

FILE_UPLOAD = "test_image.png"
# FILE_UPLOAD = "test_image1.png"

UPLOAD_PATH = 'C:\\fakepath\\test_image.png'
FILE_DOWNLOAD = "sampleFile.jpeg"

# TEXT_RESULTS = f"You have selected :\nhome\ndesktop\nnotes\ncommands\ndocuments\nworkspace\nreact\nangular\nveu" \
#                f"\noffice\npublic\nprivate\nclassified\ngeneral\ndownloads\nwordFile\nexcelFile"
TEXT_RESULTS = f"You have selected :\ndesktop\nnotes\ncommands\ndownloads\nwordFile\nexcelFile"
