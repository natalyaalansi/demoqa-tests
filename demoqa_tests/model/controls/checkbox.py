from typing import Tuple

import selene
from selene import have
from demoqa_tests.model.data.user import Hobby

class Checkbox:
    def __init__(self, elements: selene.Element):
        self.elements = elements

    def check_options(self, options: Tuple[Hobby]):
        for option in options:
            self.elements.by(have.exact_text(option)).first.element('..').click()
        return self