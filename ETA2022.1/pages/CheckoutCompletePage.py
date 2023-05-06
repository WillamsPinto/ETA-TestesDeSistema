from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CheckoutCompletePage(PageObject):

    url = 'https://www.saucedemo.com/checkout-complete.html'
    txt_checkout_title = 'Checkout: Complete!'
    id_finish_btn = 'finish'
    id_back_products_btn = 'back-to-products'
    txt_header_msg_complete = 'Thank you for your order!'
    class_msg_header_complete = 'complete-header'
    class_msg_complete = 'complete-text'
    txt_msg_complete = 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'


    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_checkout_information_page(self):
        return self.is_page(self.url, self.txt_checkout_title)

    def total_value(self):
        subtotal = float(self.driver.find_element(By.CLASS_NAME, self.class_summary_subtotal_item).text)
        tax = float(self.driver.find_element(By.CLASS_NAME, self.class_summary_tax_label).text)
        return self.driver.find_element(By.CLASS_NAME, self.class_summary_total_label == (subtotal+tax).__str__())

    def click_finish_btn(self):
        self.driver.find_element(By.ID, self.id_finish_btn).click()

    def has_header_complete_msg(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_msg_header_complete).text == self.txt_header_msg_complete

    def has_txt_complete_msg(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_msg_complete).text == self.txt_msg_complete
