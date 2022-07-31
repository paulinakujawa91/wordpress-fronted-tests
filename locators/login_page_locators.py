from selenium.webdriver.common.by import By


class LoginPageLocators:
    login = (By.ID, 'user_login')
    password = (By.ID, 'user_pass')
    login_button = (By.ID, 'wp-submit')
    error_msg = (By.ID, 'login_error')