from selenium.webdriver.common.by import By
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "email")
        self.password_textbox = (By.ID, "password")
        self.pre_login_button = (By.ID, "prelogin_button")
        self.login_button = (By.ID, "login_button")
        self.cookies_accept = (By.ID, "CybotCookiebotDialogBodyButtonAccept")
        self.login_google_iframe = (By.XPATH, "//*[starts-with(@id,'gsi_')]")
        self.login_google_btn = (By.ID, "button-label")
        self.login_microsoft_btn = (By.ID, "ms-button")
        self.microsoft_email = (By.ID, "i0116")
        self.microsoft_login_btn = (By.ID, "idSIButton9")
        self.microsoft_password = (By.ID, "i0118")
        self.microsoft_signin_btn = (By.ID, "idSIButton9")
        self.microsoft_decline = (By.ID, "declineButton")
        self.welcome_menu = (By.ID, "welcome")
        self.password_error = (By.CSS_SELECTOR, ".password_error")


    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_pre_login(self):
        self.driver.find_element(*self.pre_login_button).click()

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def accept_cookies(self):
        self.driver.find_element(*self.cookies_accept).click()

    def login_google(self):
        self.driver.find_element(*self.login_google_iframe)
        self.driver.switch_to.frame(self.login_google_iframe)
        self.driver.find_element(self.login_google_btn).click()

    def login_microsoft(self):
        self.driver.find_element(*self.login_microsoft_btn).click()

    def enter_microsoft_email(self, email):
        self.driver.find_element(*self.microsoft_email).send_keys(email)

    def press_microsoft_login(self):
        self.driver.find_element(*self.microsoft_login_btn).click()

    def enter_microsoft_password(self, password):
        self.driver.find_element(*self.microsoft_password).send_keys(password)

    def microsoft_signin(self):
        self.driver.find_element(*self.microsoft_signin_btn).click()
        time.sleep(2)
        self.driver.find_element(*self.microsoft_decline).click()

    def verify_successful_login(self):
        if self.driver.find_element(*self.welcome_menu).is_displayed():
            print("Logged in succesfully!")
        else:
            print("Error in login")

    def verify_unsuccessful_login(self):
        if self.driver.find_element(*self.password_error).is_displayed():
            print("Wrong Credentials")
        else:
            print("Error in login")