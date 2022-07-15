import math

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators as PP


class ProductPage(BasePage):
    def add_to_cart(self):
        self.should_be_add_to_cart_btn()
        self.browser.find_element(*PP.ADD_TO_CART_BTN).click()

    def should_be_add_to_cart_btn(self):
        assert self.is_element_present(*PP.ADD_TO_CART_BTN)

    def switch_to_alert(self):
        try:
            return self.browser.switch_to.alert
        except NoAlertPresentException:
            # raise NoAlertPresentException('Нет доступных оповещений для переключения.')
            assert False, 'Нет доступных оповещений для переключения.'

    def solve_quiz_and_get_code(self):
        alert = self.switch_to_alert()
        x = alert.text.split('\n')[0][4:]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        sec_alert = self.switch_to_alert()
        alert_text = sec_alert.text
        print(f"Ваш код: {alert_text}")
        sec_alert.accept()

    def is_product_name_equal_product_name_in_cart(self):
        product_name = self.browser.find_element(*PP.PRODUCT_NAME).text
        product_name_in_cart = self.browser.find_element(*PP.PRODUCT_NAME_IN_CART).text
        print(
            f'{product_name} - название товара на странице \n{product_name_in_cart} - название товара добавленного в корзину')
        assert product_name == product_name_in_cart, \
            'Названия товара,добавленного в корзину не соотвествует названию на странце'

    def is_price_in_cart_equal_product_price(self):
        product_price = self.browser.find_element(*PP.PRODUCT_PRICE).text
        price_in_cart = self.browser.find_element(*PP.CART_PRICE).text
        print(
            f'{product_price} - цена товара \n{price_in_cart} - цена в корзине')
        assert product_price == price_in_cart, 'Цена товара не соотвествует цене в корзине'
