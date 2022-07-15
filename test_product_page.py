import time

from .pages.product_page import ProductPage
import pytest

def get_data_for_parametrize():
    product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    return [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


@pytest.mark.parametrize('link', get_data_for_parametrize())
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.is_product_name_equal_product_name_in_cart()
    page.is_price_in_cart_equal_product_price()
