from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CheckoutOverviewPage(PageObject):

    url = 'https://www.saucedemo.com/checkout-step-two.html'
    txt_checkout_title = 'Checkout: Overview'
    id_finish_btn = 'finish'
    txt_error_first_name_msg = 'Error: First Name is required'
    class_error_first_name = 'error-message-container'
    class_inventory_item_price = 'inventory_item_price'
    class_summary_info_label = 'summary_info_label'
    class_summary_value_label = 'summary_value_label'
    class_summary_subtotal_item = 'summary_subtotal_label'
    class_summary_tax_label = 'summary_tax_label'
    class_summary_total_label = 'summary_total_label'
    txt_payment_information = 'Payment Information'
    txt_shipping_information = 'Shipping Information'
    txt_price_total = 'Price Total'


    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_checkout_information_page(self):
        return self.is_page(self.url, self.txt_checkout_title)

    def has_same_price(self, price):
        return self.driver.find_element(By.CLASS_NAME, self.class_inventory_item_price).text == price

    def has_a_payment_information_title(self):
        info_labels_list = self.driver.find_elements(By.CLASS_NAME, self.class_summary_info_label)
        return info_labels_list[0].text == self.txt_payment_information

    def has_a_shipping_information_title(self):
        info_labels_list = self.driver.find_elements(By.CLASS_NAME, self.class_summary_info_label)
        return info_labels_list[1].text == self.txt_shipping_information

    def has_a_price_total_title(self):
        info_labels_list = self.driver.find_elements(By.CLASS_NAME, self.class_summary_info_label)
        return info_labels_list[2].text == self.txt_price_total

    def total_value_is_correct(self):
        subtotal = self.driver.find_element(By.CLASS_NAME, self.class_summary_subtotal_item).text.translate(str.maketrans('', '', 'Item total: $'))
        tax = self.driver.find_element(By.CLASS_NAME, self.class_summary_tax_label).text.translate(str.maketrans('', '', 'Tax: $'))
        subtotal = float(subtotal)
        tax = float(tax)
        total_label_value = float(self.driver.find_element(By.CLASS_NAME, self.class_summary_total_label).text.translate(str.maketrans('', '', 'Total: $')))
        return total_label_value == subtotal + tax

    def click_finish_btn(self):
        self.driver.find_element(By.ID, self.id_finish_btn).click()