from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, 'input#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, 'input#id_login-password')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, 'input#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, 'input#id_registration-password1')
    CONFIRM_REGISTRATION_PASSWORD = (By.CSS_SELECTOR, 'input#id_registration-password2')


class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) .alertinner  strong')
    CART_PRICE = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) .alertinner  strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main p:nth-child(2)')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
