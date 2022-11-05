from selene.support.shared import browser
import selene

def rows(*, inside: selene.Browser | selene.Element = browser):
    return inside.all('tbody tr')