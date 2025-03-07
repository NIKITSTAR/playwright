from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ''

    def login(self, username, password):
        self.navigate_to()
        self.wait_for_selector_and_fill(LoginPageLocators.USERNAME, username)
        self.wait_for_selector_and_fill(LoginPageLocators.PASSWORD, password)
        self.wait_for_selector_and_click(LoginPageLocators.BUTTON_LOGIN)
        self.assert_text_present_on_page('Products')