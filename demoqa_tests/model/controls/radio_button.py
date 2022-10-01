from selene.support.shared import browser

def set_option(number: int):
    browser.element(f'[for=gender-radio-{number}]').click()