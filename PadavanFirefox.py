import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture()
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get('http://149.255.118.78:7080')
    yield driver
    driver.close()

if __name__ == '__main__':
    pytest.main()

def test_auth_positiv(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, 'loginEmail')))
    login.send_keys('test@protei.ru')

    password = driver.find_element(by=By.ID, value='loginPassword')
    password.send_keys('test')

    button = driver.find_element(by=By.ID, value='authButton')
    button.click()

    main_title = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, 'h3')))
    assert main_title.is_displayed()
    assert main_title.get_attribute('class') == 'uk-card-title'
    assert main_title.text == 'Добро пожаловать!'

def test_auth_negativ_invalid_password(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, 'loginEmail')))
    login.send_keys('test@protei.ru')

    password = driver.find_element(by=By.ID, value='loginPassword')
    password.send_keys('12345')

    button = driver.find_element(by=By.ID, value='authButton')
    button.click()

    error_message = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, 'KEKEKEKEKEKKEKE')))
    assert error_message.get_attribute('class') == 'uk-alert uk-alert-danger'
    assert error_message.text == 'Неверный E-Mail или пароль'

def test_auth_negativ_invalid_email(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, 'loginEmail')))
    login.send_keys('12345@protei.ru')

    password = driver.find_element(by=By.ID, value='loginPassword')
    password.send_keys('test')

    button = driver.find_element(by=By.ID, value='authButton')
    button.click()

    error_message = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, 'KEKEKEKEKEKKEKE')))
    assert error_message.get_attribute('class') == 'uk-alert uk-alert-danger'
    assert error_message.text == 'Неверный E-Mail или пароль'

def test_auth_negativ_incorrect_email_1(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, 'loginEmail')))
    login.send_keys('12345')

    password = driver.find_element(by=By.ID, value='loginPassword')
    password.send_keys('test')

    button = driver.find_element(by=By.ID, value='authButton')
    button.click()

    error_message = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, 'emailFormatError')))
    assert error_message.get_attribute('class') == 'uk-alert uk-alert-danger'
    assert error_message.text == 'Неверный формат E-Mail'

def test_auth_negativ_incorrect_email_2(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, 'loginEmail')))
    login.send_keys('@protei.ru')

    password = driver.find_element(by=By.ID, value='loginPassword')
    password.send_keys('test')

    button = driver.find_element(by=By.ID, value='authButton')
    button.click()

    error_message = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, 'emailFormatError')))
    assert error_message.get_attribute('class') == 'uk-alert uk-alert-danger'
    assert error_message.text == 'Неверный формат E-Mail'

def test_auth_negativ_incorrect_email_3(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, 'loginEmail')))
    login.send_keys('12345@')

    password = driver.find_element(by=By.ID, value='loginPassword')
    password.send_keys('test')

    button = driver.find_element(by=By.ID, value='authButton')
    button.click()

    error_message = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, 'emailFormatError')))
    assert error_message.get_attribute('class') == 'uk-alert uk-alert-danger'
    assert error_message.text == 'Неверный формат E-Mail'