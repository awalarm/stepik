from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_in_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def should_be_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text\
               == self.browser.find_element(*ProductPageLocators.NOTICE_ADD_PRODUCT).text

    def should_be_same_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text\
               in self.browser.find_element(*ProductPageLocators.NOTICE_PRICE_PRODUCT).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message2(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"
