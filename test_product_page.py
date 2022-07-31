import time

import allure
import pytest

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.locators import URLs
from .pages.login_page import LoginPage


def get_data_for_parametrize():
    # product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    # links = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
    links = [['http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'],
             ['http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'],
             ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019']]
    return links[-1]


@pytest.mark.parametrize('link', get_data_for_parametrize())
class TestProductPage:
    @allure.step('Проверка на добавление незарегистрированным пользователем товара в корзину.')
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.is_product_name_equal_product_name_in_cart()
        page.is_price_in_cart_equal_product_price()

    @allure.step(
        'Проверка на отсутсвие оповещения об успешном добавлении товара в корзину незарегистрированным пользователем.')
    @pytest.mark.xfail(
        reason="Отрицательная проверка: при добавлении товара в корзину появляется оповещение об успещном добавлении.")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()

    @allure.step(
        'Проверка на исчезновении оповещения об успешном добавлении товра в корзину.')
    @pytest.mark.xfail(
        reason="Отрицательная проверка: при добавлении товара в корзину оповещение об успещном добавлении не исчезает.")
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.is_success_message_disappeared()

    @allure.step(
        'Проверка на видимость кнопки авторизации незарегистрированным пользоватлем.')
    def test_guest_should_see_login_link_on_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @allure.step('Проверка на возможность перехода авторизованного пользователя на странницу авторизации.')
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    @allure.step(
        'Проверка на видимость незарегистрированным пользоватлем товаров в корзине при переходе с страницы товара.')
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.is_basket_empty()
        basket_page.is_present_basket_empty_text()

    @allure.step(
        'Проверка на отсутсвие видимости неавторизованным пользователем сообщения об успешном добавлении товара в '
        'корзину, без добавления товара в корзину.')
    def test_guest_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.parametrize('link', get_data_for_parametrize())
class TestUserAddToBasketFromProductPage:
    @allure.step('Создание пользователя.')
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, URLs.LOGIN_PAGE_URL)
        login_page.open()
        login_page.register_new_user(f'{time.time()}@qwe.com', time.time() + 1)
        login_page.should_be_authorized_user()

    @allure.step(
        'Проверка на отсутсвие видимости авторизованным пользователем сообщения об успешнои добавлении товара в '
        'корзину.')
    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @allure.step('Проверка возможность добавления авторизованным пользователем товара в корзину.')
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.is_product_name_equal_product_name_in_cart()
        page.is_price_in_cart_equal_product_price()
