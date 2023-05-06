from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class YourCart(PageObject):

    url = 'https://www.saucedemo.com/cart.html'
    txt_your_cart_title = 'Your Cart'
    id_checkout_btn = 'checkout'
    class_inventory_item_price = 'inventory_item_price'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_your_cart_page(self):
        return self.is_page(self.url, self.txt_your_cart_title)

    def click_checkout(self):
        self.driver.find_element(By.ID, self.id_checkout_btn).click()

    def get_item_price(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_inventory_item_price).text