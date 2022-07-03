from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button(browser):
    browser.get(link)
    time.sleep(5)
    button_add = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')[0].text
    assert button_add == 'Añadir al carrito', "Текст кнопки не совпадает"
