from selene.support.shared import browser
import pytest
import os

@pytest.fixture(scope='function', autouse='True')
def browser_management():
    browser.config.base_url = os.getenv('selene.base_url', 'https://demoqa.com')
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))
    browser.config.window_height = int(os.getenv('selene.window_height', '900'))
    browser.config.window_width = int(os.getenv('selene.window_width', '1200'))

    yield

