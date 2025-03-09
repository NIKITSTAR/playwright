from playwright.sync_api import Page
from locators.checkout_page_locators import CheckoutPageLocators
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page: Page) -> None:
        """Инициализирует объект CheckoutPage.page: Экземпляр страницы Playwright."""
        super().__init__(page)
        self._endpoint: str = 'checkout-step-one.html'

    def start_checkout(self) -> None:
        """Начинает процесс оформления заказа, проверяет наличие поля для ввода имени"""
        self.wait_for_selector_and_click(CheckoutPageLocators.BUTTON_CHECKOUT)
        self.assert_element_is_visible(CheckoutPageLocators.TEXT_FIRST_NAME)

    def fill_personal_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Заполняет форму личных данных на странице оформления заказа.
        Args:
            first_name: Имя пользователя.
            last_name: Фамилия пользователя.
            postal_code: Почтовый индекс."""
        self.wait_for_selector_and_type(CheckoutPageLocators.TEXT_FIRST_NAME, first_name, 100)
        self.wait_for_selector_and_type(CheckoutPageLocators.TEXT_LAST_NAME, last_name, 100)
        self.wait_for_selector_and_type(CheckoutPageLocators.TEXT_POSTAL_CODE, postal_code, 100)
        self.assert_input_value(CheckoutPageLocators.TEXT_POSTAL_CODE, postal_code)

    def click_continue(self) -> None:
        """Завершает оформление заказа, проверяет, что на странице присутствует сообщение об успешном оформлении заказа."""
        self.wait_for_selector_and_click(CheckoutPageLocators.BUTTON_CONTINUE)
        self.wait_for_selector_and_click(CheckoutPageLocators.BUTTON_FINISH)
        self.assert_text_present_on_page('Thank you for your order!')

