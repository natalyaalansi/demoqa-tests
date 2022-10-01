import datetime

import selene
from selene.support.shared import browser
import demoqa_tests
from selenium.webdriver.common.keys import Keys

def set_date(element: selene.Element, date: datetime.date):
    element.send_keys(
        Keys.CONTROL + 'a' + Keys.NULL,
        date.strftime(demoqa_tests.config.datetime_format),
    ).press_enter()