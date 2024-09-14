import pytest
from selenium import webdriver
import time
from Pages.login_page import LoginPage

#Variables
options = webdriver.FirefoxOptions()
options.page_load_strategy = 'normal'
email = 'peteyodeck2@outlook.com'
password = 'User!995'

# Initialize Firefox webdriver , Set Up and Teardown
@pytest.fixture()
def driver():
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

#Tests
def test_login_microsoft(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://app.yodeck.com/login")
    time.sleep(4)
    login_page.accept_cookies()
    time.sleep(2)
    parent_win = driver.current_window_handle
    login_page.login_microsoft()
    time.sleep(5)
    windows = driver.window_handles
    for w in windows:
        driver.switch_to.window(w)
        if driver.title.__eq__("Sign in to your account"):
            login_page.enter_microsoft_email(email)
            time.sleep(2)
            login_page.press_microsoft_login()
            time.sleep(2)
            login_page.enter_microsoft_password(password)
            time.sleep(2)
            login_page.microsoft_signin()
            time.sleep(3)
            driver.switch_to.window(parent_win)
            time.sleep(4)
            login_page.verify_succesful_login()
            break

