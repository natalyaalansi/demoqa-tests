from selene import have, command
from selene.support.shared import browser


def given_opened_practice_form_page():
    browser.open('/automation-practice-form')
    ads = browser.all('[id^=google_ads_][id$=container__]')
    if ads.wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)
