from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


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
