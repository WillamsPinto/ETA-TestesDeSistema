from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CheckoutInformationPage(PageObject):

    url = 'https://www.saucedemo.com/checkout-step-one.html'
    txt_checkout_title = 'Checkout: Your Information'
    id_continue_btn = 'continue'
    txt_error_first_name_msg = 'Error: First Name is required'
    class_error_first_name = 'error-message-container'
    id_first_name = 'first-name'
    id_last_name = 'last-name'
    id_postal_code = 'postal-code'
    example_first_name = 'David'
    example_last_name = 'Ferreira'
    example_postal_code = '51544250'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_checkout_information_page(self):
        return self.is_page(self.url, self.txt_checkout_title)

    def insert_first_name(self):
        self.driver.find_element(By.ID, self.id_first_name).send_keys(self.example_first_name)

    def insert_last_name(self):
        self.driver.find_element(By.ID, self.id_last_name).send_keys(self.example_last_name)

    def insert_postal_code(self):
        self.driver.find_element(By.ID, self.id_postal_code).send_keys(self.example_postal_code)

    def click_continue(self):
        self.driver.find_element(By.ID, self.id_continue_btn).click()

    def has_first_name_error(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_error_first_name).text == self.txt_error_first_name_msg
