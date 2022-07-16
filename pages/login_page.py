from .base_page import BasePage
from .locators import LoginPageLocators as LP


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'URL логина не содержит подстроки \'login\''

    def should_be_login_form(self):
        assert self.is_element_present(*LP.LOGIN_EMAIL), "Нет формы ввода почты при авторизации"
        assert self.is_element_present(*LP.LOGIN_PASSWORD), "Нет формы ввода пароля при авторизации"

    def should_be_register_form(self):
        assert self.is_element_present(*LP.REGISTRATION_EMAIL), "Нет формы ввода почты при регистрации"
        assert self.is_element_present(*LP.REGISTRATION_PASSWORD), "Нет формы ввода первого пароля при регистрации"
        assert self.is_element_present(
            *LP.CONFIRM_REGISTRATION_PASSWORD), "Нет формы ввода второго пароля при регистрации"
