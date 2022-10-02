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

def set_date2():
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__year-select').element('[value="1993"]').click()
    browser.element('.react-datepicker__month-select').element('[value="7"]').click()
    browser.element('.react-datepicker__day--024').click()
    return set_date2()