import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    @allure.step('Открытие браузера.')
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except (NoSuchElementException, TimeoutException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def get_present_element(self, how, what):
        if self.is_element_present(how, what):
            return self.browser.find_element(how, what)
        else:
            assert self.is_element_present(how, what), f'Элемент с локатором {how} :: {what} не найден'

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def switch_to_alert(self, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.alert_is_present())
            return self.browser.switch_to.alert
        except (NoAlertPresentException, TimeoutException):
            raise NoAlertPresentException('Нет доступных оповещений для переключения.')
            # assert False, 'Нет доступных оповещений для переключения.'

    @allure.step('Переход на страницу авторизации.')
    def go_to_login_page(self):
        login_link = self.get_present_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    @allure.step('Проверка на видимость кнопки авторизации.')
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Ссылка на страницу авторизации не отображается"

    @allure.step('Переход в корзину.')
    def go_to_basket(self):
        self.get_present_element(*BasePageLocators.BASKET_HEADER).click()

    @allure.step('Проверка на появление сообщении о неавторизованном пользователе.')
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
