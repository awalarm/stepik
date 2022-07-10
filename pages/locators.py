from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASCKET = (By.LINK_TEXT, "View basket")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class BasketPageLocators:
    BASKET_IS_EMPTY = (By.XPATH, "//div[@id='content_inner']/p")


class LoginPageLocators:
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FIELD_LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    FIELD_LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    BUTTON_LOGIN = (By.NAME, "login_submit")

    FORM_REGISTER = (By.CSS_SELECTOR, "#register_form")
    FIELD_REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    FIELD_REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    FIELD_REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.NAME, "registration_submit")


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NOTICE_ADD_PRODUCT = (By.CSS_SELECTOR, "div.alertinner strong")
    NOTICE_PRICE_PRODUCT = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/p[contains(@class, 'price_color')]")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
