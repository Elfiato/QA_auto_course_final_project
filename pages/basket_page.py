import allure

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    @allure.step('Проверка на отсутсвие товаров в корзине.')
    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), 'В корзине присутствуют элементы.'

    @allure.step('Проверка на наличие текста о пустой корзине.')
    def is_present_basket_empty_text(self):
        basket_empty_text = self.get_present_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
        print(basket_empty_text)
        assert basket_empty_text == 'Your basket is empty. Continue shopping', 'Отсутсвует надпись \'Your basket is ' \
                                                                               'empty.\' '
