from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url_for_check = self.browser.current_url
        assert 'login' in url_for_check, "word \"login\" not in url"

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not present"
        assert True

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Register form is not present"
        assert True
