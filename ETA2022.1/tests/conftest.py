import pytest

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Set browser")

@pytest.fixture()
def choose_browser(request):
    selected_browser = request.config.getoption("--browser").lower()
    yield selected_browser

@pytest.fixture()
def open_login(choose_browser):
    print("open_login")
    login_page = LoginPage(browser=choose_browser)
    yield login_page
    print("close login")
    login_page.close()

@pytest.fixture()
def efetuar_login(open_login):
    print("efetuar login")
    open_login.efetuar_login()
    yield open_login

@pytest.fixture()
def add_product_to_cart(efetuar_login):
    products_page = ProductsPage(driver=efetuar_login.driver)
    products_page.add_first_product_to_cart()
    yield products_page

