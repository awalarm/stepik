import pytest
import time

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

email = str(time.time()) + "@fakemail.org"


@pytest.fixture()
def setup(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.register_new_user(email, "12qwas34er")
    page.should_be_authorized_user()


class TestUserAddToBasketFromProductPage:

    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.add_product_in_cart()
        # page.solve_quiz_and_get_code()
        # page.should_be_product_name()
        # page.should_be_same_price()
        page.should_not_be_success_message2()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_view_bascket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.is_empty_basket()

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_in_cart()
        page.should_not_be_success_message()

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
    def test_guest_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
