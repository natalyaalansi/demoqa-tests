import selene
from selene import have
from selene.support.shared import browser

class DropDown:
    def __init__(self, element: selene.Element):
        self.element = element

    def select(self, option):
        self.element.click()
        browser.all('[id^=react-select][id*=-option-]').by(
            have.exact_text(option)
        ).first.click()
        return self
