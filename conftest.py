import allure
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default="en", help="Choose browser: Choose launge: es, ru or en")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    if browser_name == "chrome":
        with allure.step('Выбран браузер Google Chrome'):
            options = webdriver.ChromeOptions()
            options.add_experimental_option('prefs', {'intl.accept_languages': language})
            driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        with allure.step('Выбран браузер Mozilla Firefox'):
            options = webdriver.FirefoxProfile()
            options.set_preference("intl.accept_languages", language)
            driver = webdriver.Firefox(firefox_profile=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    driver.quit()
