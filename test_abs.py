import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser2():
    print("\nstart browser for test..")
    browser1 = webdriver.Chrome()
    yield browser1
    print("\n quit browser...\n")
    browser1.quit()


@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser2, prepare_faces, very_important_fixture):
        browser2.get(link)
        browser2.find_element_by_css_selector("#login_link")

    @pytest.mark.regress
    def test_guest_should_see_basket_link_on_the_main_page(self, browser2, prepare_faces):
        browser2.get(link)
        browser2.find_element_by_css_selector(".basket-mini .btn-group > a")