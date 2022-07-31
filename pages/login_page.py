import allure

from .base_page import BasePage
from .locators import LoginPageLocators as LP


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    @allure.step('Проверка на наличие подстроки \'login\' в URL страницы авторизации.')
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'URL логина не содержит подстроки \'login\''

    @allure.step('Проверка на наличие форм для авторизации на странице авторизации.')
    def should_be_login_form(self):
        assert self.is_element_present(*LP.LOGIN_EMAIL), "Нет формы ввода почты при авторизации"
        assert self.is_element_present(*LP.LOGIN_PASSWORD), "Нет формы ввода пароля при авторизации"

    @allure.step('Проверка на наличие форм для регистрации на странице авторизации.')
    def should_be_register_form(self):
        assert self.is_element_present(*LP.REGISTRATION_EMAIL), "Нет формы ввода почты при регистрации"
        assert self.is_element_present(*LP.REGISTRATION_PASSWORD), "Нет формы ввода первого пароля при регистрации"
        assert self.is_element_present(
            *LP.CONFIRM_REGISTRATION_PASSWORD), "Нет формы ввода второго пароля при регистрации"

    @allure.step('Регистрация нового пользователя.')
    def register_new_user(self, email, password):
        self.get_present_element(*LP.REGISTRATION_EMAIL).send_keys(email)
        self.get_present_element(*LP.REGISTRATION_PASSWORD).send_keys(password)
        self.get_present_element(*LP.CONFIRM_REGISTRATION_PASSWORD).send_keys(password)
        self.get_present_element(*LP.REGISTRATION_SUBMIT_BTN).click()
