from selenium.webdriver.common.by import By
import time


class ImagePage:

    def __init__(self, driver):
        self.driver = driver
        self.add_image_btn = (By.CSS_SELECTOR, ".openGallery")
        self.upload_image_input = (By.ID, "image-file-uploader")
        self.input_url = (By.CSS_SELECTOR, "#import_image_from_url > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
        self.go_to_media_btn = (By.ID, "media_menu")
        self.go_to_images_btn = (By.ID, "media_images")
        self.modal_dialog = (By.CSS_SELECTOR, ".bootbox")
        self.upload_image_btn = (By.XPATH, "//button[text()='Upload']")
        self.save_btn = (By.XPATH, "//button[text()='Save']")
        self.import_url_btn = (By.XPATH, "//a[text()='IMPORT FROM URL']")
        self.input_url = (By.XPATH, "//input[@type='text' and @name='import-image-url']")
        self.name_image = (By.ID, "c352_name")

    def go_to_media(self):
        self.driver.find_element(*self.go_to_media_btn).click()

    def go_to_images(self):
        self.driver.find_element(*self.go_to_images_btn).click()


    def add_new_image(self):
        self.driver.find_element(*self.add_image_btn).click()

    def upload_new_image(self, imagepath):
        self.driver.find_element(*self.upload_image_input).send_keys(imagepath)

    def upload_image(self):
        self.driver.find_element(*self.upload_image_btn).click()

    def click_save(self):
        self.driver.find_element(*self.save_btn).click()

    def import_from_url(self):
        self.driver.find_element(*self.import_url_btn).click()

    def enter_image_url(self, image_url):
        self.driver.find_element(*self.input_url).send_keys(image_url)

    def enter_image_name(self, image_name):
        self.driver.find_element(*self.name_image).send_keys(image_name)

