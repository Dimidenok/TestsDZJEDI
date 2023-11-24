import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from PageObjects import SearchHelper

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()

if __name__ == '__main__':
    pytest.main()


def test_auth_positiv(driver):
    authtorization_page = SearchHelper(driver)
    authtorization_page.go_to_site()
    authtorization_page.enter_email('test@protei.ru')
    authtorization_page.enter_password('test')
    authtorization_page.click_on_the_button()
    main_title = authtorization_page.search_main_title()
    assert main_title.is_displayed()
    assert main_title.get_attribute('class') == 'uk-card-title'
    assert main_title.text == 'Добро пожаловать!'

def test_auth_negativ_invalid_password(driver):
    authtorization_page = SearchHelper(driver)
    authtorization_page.go_to_site()
    authtorization_page.enter_email('test@protei.ru')
    authtorization_page.enter_password('12345')
    authtorization_page.click_on_the_button()
    error_message = authtorization_page.search_error_message()
    assert error_message.get_attribute('class') == 'uk-alert uk-alert-danger'
    assert error_message.text == ('Неверный E-Mail или пароль')

def test_auth_negativ_invalid_email(driver):
    authtorization_page = SearchHelper(driver)
    authtorization_page.go_to_site()
    authtorization_page.enter_email('12345@protei.ru')
    authtorization_page.enter_password('test')
    authtorization_page.click_on_the_button()
    error_message = authtorization_page.search_error_message()
    assert error_message.get_attribute('class') == 'uk-alert uk-alert-danger'
    assert error_message.text == ('Неверный E-Mail или пароль' )

def test_auth_negativ_incorrect_email_1(driver):
    authtorization_page = SearchHelper(driver)
    authtorization_page.go_to_site()
    authtorization_page.enter_email('12345')
    authtorization_page.enter_password('test')
    authtorization_page.click_on_the_button()
    error_message = authtorization_page.search_error_message()
    assert error_message.get_attribute('class') == 'uk-alert uk-alert-danger'
    assert  error_message.text == ('Неверный формат E-Mail')

def test_auth_negativ_incorrect_email_2(driver):
    authtorization_page = SearchHelper(driver)
    authtorization_page.go_to_site()
    authtorization_page.enter_email('@protei.ru')
    authtorization_page.enter_password('test')
    authtorization_page.click_on_the_button()
    error_message = authtorization_page.search_error_message()
    assert error_message.get_attribute('class') == 'uk-alert uk-alert-danger'
    assert error_message.text == ('Неверный формат E-Mail')

def test_auth_negativ_incorrect_email_3(driver):
    authtorization_page = SearchHelper(driver)
    authtorization_page.go_to_site()
    authtorization_page.enter_email('12345@')
    authtorization_page.enter_password('test')
    authtorization_page.click_on_the_button()
    error_message = authtorization_page.search_error_message()
    assert error_message.get_attribute('class') == 'uk-alert uk-alert-danger'
    assert error_message.text == ('Неверный формат E-Mail')

