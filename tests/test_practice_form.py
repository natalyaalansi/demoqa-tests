from selene.support.shared import browser
from demoqa_tests.model import app
from demoqa_tests.utils import path
from selene import have, command


def test_submit_practise_form():

    app.given_opened_practice_form_page()

    # WHEN
    browser.element('#firstName').type('natalya')
    browser.element('#lastName').type('alansi')
    browser.element('#userEmail').type('nalansi@yahoo.com')
    browser.element('[id^=gender-radio][value=Male]').element('..').click()
    browser.element('#userNumber').type('0123456789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').send_keys('1993')
    browser.element('.react-datepicker__month-select').send_keys('July')
    browser.element(f'.react-datepicker__day--0{24}').click()
    browser.element('#subjectsInput').perform(command.js.scroll_into_view)
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.all('[id^=hobbies]').by(have.value('1')).first.element('..').click()
    browser.element('#uploadPicture').send_keys(path.to_resource('minion.png'))
    browser.element('#currentAddress').type('Tbilisi')
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=-option-]').by(have.exact_text('NCR')).first.click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=-option-]').by(have.exact_text('Delhi')).first.click()
    browser.element('#submit').perform(command.js.click)

    # THEN
    dialog_table = browser.element('.modal-content').element('.table')
    rows = dialog_table.all('tbody tr')
    rows.should(have.texts(
        'natalya alansi',
        'nalansi@yahoo.com',
        'Male',
        '0123456789',
        '24 July,1993',
        'Computer Science',
        'Sports',
        'minion.png',
        'Tbilisi',
        'NCR Delhi'
    ))

