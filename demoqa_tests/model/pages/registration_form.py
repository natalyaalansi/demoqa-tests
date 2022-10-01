from selene import have, command
from selene.support.shared import browser
from demoqa_tests.model.controls import dropdown, radio_button, datepicker, checkbox, file_upload
from demoqa_tests.model.data import user
import datetime

state = browser.element('#state')

def given_opened():
    browser.open('/automation-practice-form')
    ads = browser.all('[id^=google_ads_][id$=container__]')
    if ads.wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)

def fill_full_name(name: str, surname: str):
    browser.element('#firstName').type(name)
    browser.element('#lastName').type(surname)

def fill_email(value: str):
    browser.element('#userEmail').type(value)

def select_gender(value: user.Gender):
    radio_button.set_option(value.value) #noqa

def fill_phone_number(value: str):
    browser.element('#userNumber').type(value)

def select_birthday(date: datetime.date):
    datepicker.set_date(browser.element('#dateOfBirthInput'), date)

def fill_subjects(*subjects: str):
    for subject in subjects:
        browser.element('#subjectsInput').type(subject).press_enter()

def select_hobbies(*options: user.Hobby):
    checkbox.check_options(
        browser.all('[for^=hobbies-checkbox]'), *[option.value for option in options]
    )

def select_picture(relative_path):
    file_upload.upload(relative_path)

def fill_address(value: str):
    browser.element('#currentAddress').type(value)

def scroll_to_bottom():
    state.perform(command.js.scroll_into_view)

def set_state(value: str):
    dropdown.select(state, value)

def set_city(value: str):
    dropdown.select(browser.element('#city'), value)

def submit():
    browser.element('#submit').perform(command.js.click)

def check_submitted_user(information):
    dialog_table = browser.element('.modal-content').element('.table')
    rows = dialog_table.all('tbody tr')
    for row, value in information:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
