import random
import pytest
from pages.login_page import LoginPage
from tests import const


@pytest.mark.usefixtures('setup')
class TestOpenLoginPage:

    def test_log_in_correct_data(self):
        login_page = LoginPage(self.driver)

        login_page.log_in(const.login,const.password)

        assert login_page.is_login_successfuly()

    def test_log_in_invalid_login(self):
        invalid_login = str(random.randint(0,1000)) + const.login
        expected_msg = 'The username ' + invalid_login + ' is not registered on this site. If you are unsure of your username, try your email address instead.'
        login_page = LoginPage(self.driver)

        login_page.log_in(invalid_login, const.password)

        assert expected_msg in login_page.get_error_message()

    def test_log_in_invalid_password(self):
        invalid_password = str(random.randint(0,1000)) + const.password
        expected_msg = 'The password you entered for the username'
        login_page = LoginPage(self.driver)

        login_page.log_in(const.login, invalid_password)


        assert expected_msg in login_page.get_error_message()