import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class ProductsPage(PageObject):

    url = 'https://www.saucedemo.com/inventory.html'
    text_product_title = 'Products'
    class_product_item = 'inventory_item'
    id_menu = 'react-burger-menu-btn'
    class_product_item = 'inventory_item'
    tag_add_to_cart_btn = 'button'
    class_shopping_cart_badge = 'shopping_cart_badge'
    class_shopping_cart_icon = 'shopping_cart_link'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_products_page(self):
        return self.is_page(self.url, self.text_product_title)

    def count_products_page(self):
        count_products = len(self.driver.find_elements(By.CLASS_NAME, self.class_product_item))
        return count_products

    def has_menu_btn(self):
        try:
            self.driver.find_element(By.ID, self.id_menu)
            return True
        except NoSuchElementException:
            return False

    def add_first_product_to_cart(self):
        product_list_elements = self.driver.find_elements(By.CLASS_NAME, self.class_product_item)
        product_list_elements[0].find_element(By.TAG_NAME, self.tag_add_to_cart_btn).click()
        cart_number = self.driver.find_element(By.CLASS_NAME, self.class_shopping_cart_badge).text
        if cart_number != "1":
            raise Exception("Carrinho não contem 1 produto!")

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, self.class_shopping_cart_icon).click()