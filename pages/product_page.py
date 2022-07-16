import math

from selenium.common.exceptions import NoAlertPresentException, TimeoutException

from .base_page import BasePage
from .locators import ProductPageLocators as PP


class ProductPage(BasePage):
    def add_to_cart(self):
        self.should_be_add_to_cart_btn()
        self.get_present_element(*PP.ADD_TO_CART_BTN).click()

    def should_be_add_to_cart_btn(self):
        assert self.is_element_present(*PP.ADD_TO_CART_BTN), 'Кнопка добавления в корзину отсутствует.'

    def solve_quiz_and_get_code(self):
        try:
            alert = self.switch_to_alert()
            x = alert.text.split('\n')[0][4:]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()
            try:
                sec_alert = self.switch_to_alert()
                alert_text = sec_alert.text
                print(f"{alert_text}")
                sec_alert.accept()
            except NoAlertPresentException:
                print(f'На странице: {self.url}, после ввода вычисленного значения не появилось оповещения с кодом.')
        except (NoAlertPresentException, TimeoutException):
            print(f'На странице {self.url} нет необходимости вычислять значение выражения для добавления товра в '
                  f'корзину.')

    def is_product_name_equal_product_name_in_cart(self):
        product_name = self.get_present_element(*PP.PRODUCT_NAME).text
        product_name_in_cart = self.get_present_element(*PP.PRODUCT_NAME_IN_CART).text
        print(
            f'{product_name} - название товара на странице \n{product_name_in_cart} - название товара добавленного в '
            f'корзину')
        assert product_name == product_name_in_cart, \
            'Названия товара,добавленного в корзину не соотвествует названию на странце'

    def is_price_in_cart_equal_product_price(self):
        product_price = self.get_present_element(*PP.PRODUCT_PRICE).text
        price_in_cart = self.get_present_element(*PP.CART_PRICE).text
        print(
            f'{product_price} - цена товара \n{price_in_cart} - цена в корзине')
        assert product_price == price_in_cart, 'Цена товара не соотвествует цене в корзине'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *PP.PRODUCT_NAME_IN_CART), 'Оповещение о добавлении товара в корзину отображено на странице, хотя не ' \
                                       'должно там быть. '

    def is_success_message_disappeared(self):
        assert self.is_disappeared(*PP.PRODUCT_NAME_IN_CART), 'Оповещение о добавлении товара в корзину не исчезло'


