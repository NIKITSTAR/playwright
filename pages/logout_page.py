from locators.logout_page_locators import LogoutPageLocators
from pages.base_page import BasePage


class LogoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ''

    def logout(self):
        self.wait_for_selector_and_click(LogoutPageLocators.BURGER_MENU)
        self.wait_for_selector_and_click(LogoutPageLocators.BUTTON_LOGOUT)
        self.assert_element_is_visible(LogoutPageLocators.BUTTON_LOGIN)