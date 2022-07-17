import pytest

from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.locators import URLs


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, URLs.MAIN_PAGE_URL)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()
        login_page.should_be_login_form()
        login_page.should_be_register_form()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, URLs.MAIN_PAGE_URL)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, URLs.MAIN_PAGE_URL)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.is_basket_empty()
        basket_page.is_present_basket_empty_text()
