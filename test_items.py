from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button(browser):
    browser.get(link)
    time.sleep(5)
    browser.find_element(By.XPATH, "//button[text() = 'Añadir al carrito']")
