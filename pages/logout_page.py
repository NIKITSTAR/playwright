from pages.base_page import BasePage


class LogoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ''

    BURGER_SELECTOR = '#react-burger-menu-btn'
    LOGOUT_SELECTOR = '[data-test=logout-sidebar-link]'
    LOGIN_BUTTON_SELECTOR = '#login-button'

    def logout(self):
        self.wait_for_selector_and_click(self.BURGER_SELECTOR)
        self.wait_for_selector_and_click(self.LOGOUT_SELECTOR)
        self.assert_element_is_visible(self.LOGIN_BUTTON_SELECTOR)