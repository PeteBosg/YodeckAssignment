from selenium import webdriver
import time
from Pages.login_page import LoginPage
import pytest

#Variables
options = webdriver.FirefoxOptions()
options.page_load_strategy = 'normal'
email = "peterbosganas@gmail.com"
password = "Peteyodeck!995"
false_email = "false@email.com"
false_password = "Pete1234!"

# Initialize Firefox webdriver , Set Up and Teardown
@pytest.fixture()
def driver():
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

#Tests
def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://app.yodeck.com/login")
    time.sleep(3)
    login_page.accept_cookies()
    time.sleep(2)
    login_page.enter_username(email)
    time.sleep(2)
    login_page.click_pre_login()
    time.sleep(2)
    login_page.enter_password(password)
    time.sleep(2)
    login_page.click_login()
    time.sleep(4)
    login_page.verify_successful_login()


def test_login_wrong_password(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://app.yodeck.com/login")
    time.sleep(3)
    login_page.accept_cookies()
    time.sleep(2)
    login_page.enter_username(email)
    time.sleep(2)
    login_page.click_pre_login()
    time.sleep(2)
    login_page.enter_password(false_password)
    time.sleep(2)
    login_page.click_login()
    time.sleep(1)
    login_page.verify_unsuccessful_login()

def test_login_wrong_email(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://app.yodeck.com/login")
    time.sleep(3)
    login_page.accept_cookies()
    time.sleep(2)
    login_page.enter_username(false_email)
    time.sleep(2)
    login_page.click_pre_login()
    time.sleep(2)
    login_page.enter_password(password)
    time.sleep(2)
    login_page.click_login()
    time.sleep(1)
    login_page.verify_unsuccessful_login()




