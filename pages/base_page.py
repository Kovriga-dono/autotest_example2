class BasePage:
    def __init__(self, browser):
        self.browser = browser



    def find(self, args):
        return self.browser.find_element(*args)


class BasePageE:
    def __init__(self, browser_e):
        self.browser = browser_e


class BasePageF:
    def __init__(self, browser_f):
        self.browser = browser_f