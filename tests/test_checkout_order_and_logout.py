from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
import allure
from utils import attach


def test_checkout_order(context):
    page = context.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    logout_page = LogoutPage(page)

    with allure.step('Login to checkout page'):
        login_page.login('standard_user', 'secret_sauce')
        inventory_page.add_first_item_to_cart()
        checkout_page.start_checkout()
        checkout_page.fill_personal_info('John', 'Doe', '12345')
        checkout_page.click_continue()
        logout_page.logout()

    attach.add_screenshot(page)
    attach.add_html(page)
    attach.add_video(page)
