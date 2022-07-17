from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), 'В корзине присутствуют элементы.'

    def is_present_basket_empty_text(self):
        basket_empty_text = self.get_present_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
        print(basket_empty_text)
        assert basket_empty_text == 'Your basket is empty. Continue shopping', 'Отсутсвует надпись \'Your basket is ' \
                                                                               'empty.\' '
