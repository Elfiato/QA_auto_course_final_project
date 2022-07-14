from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, 'input#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, 'input#id_login-password')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, 'input#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, 'input#id_registration-password1')
    CONFIRM_REGISTRATION_PASSWORD = (By.CSS_SELECTOR, 'input#id_registration-password2')