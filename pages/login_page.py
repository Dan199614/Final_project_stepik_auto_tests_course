from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "URL login is not correct!"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert (self.is_element_present(*LoginPageLocators.LOGIN_INPUT) ==
                self.is_element_present(*LoginPageLocators.PASSWORD_INPUT) ==
                self.is_element_present(*LoginPageLocators.LOGIN_BUTTON)), "Login form not detect!"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert (self.is_element_present(*LoginPageLocators.REGISTRATION_LOGIN_INPUT) ==
                self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT) ==
                self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_RETRY_INPUT) ==
                self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON)), "Registration form not detect!"
