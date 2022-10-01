from selene.support.shared import browser
from demoqa_tests.utils import path

def upload(relative_path):
    browser.element('#uploadPicture').send_keys(path.to_resource(relative_path))