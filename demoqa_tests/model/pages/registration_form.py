from selene import have, command
from typing import Tuple
from selene.support.shared import browser
from demoqa_tests import config
from demoqa_tests.model.controls import dropdown, radio_button, checkbox, file_upload
from demoqa_tests.model.controls import modal
from demoqa_tests.model.controls.checkbox import Checkbox
from demoqa_tests.model.controls.datepicker import DatePicker
import datetime

from demoqa_tests.model.controls.dropdown import DropDown
from demoqa_tests.model.data.user import Subject, Hobby


class RegistrationForm:

    def __init__(self):
        self.state = browser.element('#state')

    def open(self): # noqa
        browser.open('/automation-practice-form')
        ads = browser.all('[id^=google_ads_][id$=container__]')
        if ads.wait.until(have.size_greater_than_or_equal(3)):
            ads.perform(command.js.remove)
        return self

    def fill_full_name(self, name: str, surname: str):
        browser.element('#firstName').type(name)
        browser.element('#lastName').type(surname)
        return self
    def fill_email(self, value: str):
        browser.element('#userEmail').type(value)
        return self

    def select_gender(self, gender):
        radio_button.set_option(gender.value) #noqa
        return self

    def fill_phone_number(self, value: str):
        browser.element('#userNumber').type(value)
        return self

    def select_birthday(self, date: datetime.date):
        DatePicker(browser.element('#dateOfBirthInput')).set_date(date)
        return self

    def fill_subjects(self, values: Tuple[Subject]):
        for subject in values:
            browser.element('#subjectsInput').send_keys(subject.value).press_enter()
        return self

    def set_hobbies(self, options: Tuple[Hobby]):
        Checkbox(browser.all('[for^=hobbies-checkbox]')).check_options([option.value for option in options])
        return self

    def select_picture(self, relative_path):
        file_upload.upload(relative_path)
        return self

    def fill_address(self, value: str):
        browser.element('#currentAddress').type(value)
        return self

    def scroll_to_bottom(self):
        self.state.perform(command.js.scroll_into_view)
        return self

    def set_state(self, value: str):
        DropDown(self.state).select(value)
        return self

    def set_city(self, value: str):
        DropDown(browser.element('#city')).select(value)
        return self

    def submit(self):
         browser.element('#submit').perform(command.js.click)
         return self

    def assert_form_sent(self, *data):
        for name, value in data:
            value = (
                value.strftime(config.datetime_view_format)
                if isinstance(value, datetime.date)
                else value
            )
            modal.rows.element_by(have.text(name)).all('td')[1].should(have.exact_text(value))
        return self