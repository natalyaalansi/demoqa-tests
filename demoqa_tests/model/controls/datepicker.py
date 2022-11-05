import datetime
import selene
import demoqa_tests
from selenium.webdriver.common.keys import Keys

class DatePicker:
    def __init__(self, element: selene.Element):
        self.element = element
    def set_date(self, date: datetime.date):
        self.element.send_keys(
            Keys.CONTROL + 'a' + Keys.NULL,
            date.strftime(demoqa_tests.config.datetime_input_format),
        ).press_enter()
        return self

#def set_date2():
#    browser.element('[id="dateOfBirthInput"]').click()
#    browser.element('.react-datepicker__year-select').element('[value="1993"]').click()
#    browser.element('.react-datepicker__month-select').element('[value="7"]').click()
#    browser.element('.react-datepicker__day--024').click()
#    return set_date2()