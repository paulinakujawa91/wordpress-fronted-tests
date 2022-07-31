from locators.home_page_locators import HomePageLocators
from locators.login_page_locators import LoginPageLocators


class LoginPage:
    test_url = 'http://localhost/wp-admin'

    def __init__(self,driver):
        self.driver = driver
        self.driver.get(self.test_url)

    def log_in(self,login,password):
        self.driver.find_element(*LoginPageLocators.login).send_keys(login)
        self.driver.find_element(*LoginPageLocators.password).send_keys(password)
        self.driver.find_element(*LoginPageLocators.login_button).click()

    def is_login_successfuly(self):
        return self.driver.find_element(*HomePageLocators.home_page_header).is_displayed()

    def get_error_message(self):
        return self.driver.find_element(*LoginPageLocators.error_msg).text
