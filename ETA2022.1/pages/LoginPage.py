from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class LoginPage(PageObject):

    # Locators
    url = 'https://www.saucedemo.com/'
    id_login_btn = 'login-button'
    class_login_error = 'error-message-container'
    text_error_login_msg = 'Epic sadface: Username is required'
    id_username = 'user-name'
    id_password = 'password'

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.open_login_page()

    def open_login_page(self):
        self.driver.get(self.url)

    def click_login_btn(self):
        self.driver.find_element(By.ID, self.id_login_btn).click()

    def is_url_login(self):
        return self.driver.current_url == self.url

    def has_login_message_error(self):
        error_msg = self.driver.find_element(By.CLASS_NAME, self.class_login_error).text
        return error_msg == self.text_error_login_msg

    def efetuar_login(self, username='standard_user', password='secret_sauce'):
        self.driver.find_element(By.ID, self.id_username).send_keys(username)
        self.driver.find_element(By.ID, self.id_password).send_keys(password)
        self.click_login_btn()

