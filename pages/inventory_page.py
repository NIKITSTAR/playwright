from locators.inventory_page_locators import InventoryPageLocators
from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'inventory.html'

    def add_first_item_to_cart(self):
        self.wait_for_selector_and_click(InventoryPageLocators.ADD_TO_CART_SELECTOR)
        self.assert_element_is_visible(InventoryPageLocators.SHOPPING_CART_LINK_SELECTOR)
        self.wait_for_selector_and_click(InventoryPageLocators.SHOPPING_CART_LINK_SELECTOR)