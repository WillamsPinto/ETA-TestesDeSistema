import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class MenuPage(PageObject):

    id_menu_burger = "react-burger-menu-btn"
    id_menu_close = "react-burger-cross-btn"
    class_menu_items = "bm-item-list"
    id_logout_menu_item = "logout_sidebar_link"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def open_menu(self):
        self.driver.find_element(By.ID, self.id_menu_burger).click()

    def is_menu_open(self):
        try:
            self.driver.find_element(By.ID, self.id_menu_close)
            self.driver.find_element(By.CLASS_NAME, self.class_menu_items)
            return True
        except NoSuchElementException:
            return False

    def click_logout(self):
        self.driver.find_element(By.ID, self.id_logout_menu_item).click()