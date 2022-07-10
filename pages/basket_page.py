from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_empty_basket(self):
        self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY)
