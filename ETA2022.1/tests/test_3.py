import time

from pages.MenuPage import MenuPage


class Test_3:

    def test_logout(self, efetuar_login):
        menu_page = MenuPage(driver=efetuar_login.driver)
        menu_page.open_menu()
        assert menu_page.is_menu_open(), "Menu is not opened!"
        menu_page.click_logout()
        assert efetuar_login.is_url_login(), "Login page not found!"

