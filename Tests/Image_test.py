from selenium import webdriver
import time
import pytest
from Tests.login_test import test_login
from Pages.images_page import ImagePage

#Variables
options = webdriver.FirefoxOptions()
options.page_load_strategy = 'normal'
email = 'peterbosganas@gmail.com'
password = 'Peteyodeck!995'
path = "C:\\Users\\User\\Desktop\\test1.jpg"
image_url = "https://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg"
image_name = "new book"



# Initialize Firefox webdriver , Set Up and Teardown
@pytest.fixture()
def driver():
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

#Tests
def test_image(driver):
    test_login(driver)
    time.sleep(2)
    image_page = ImagePage(driver)
    image_page.go_to_media()
    time.sleep(2)
    image_page.go_to_images()
    time.sleep(2)
    image_page.add_new_image()
    time.sleep(2)
    image_page.upload_new_image(path)
    time.sleep(2)
    image_page.upload_image()
    time.sleep(2)
    image_page.click_save()
    time.sleep(5)

def test_image_url(driver):
    test_login(driver)
    time.sleep(2)
    image_page = ImagePage(driver)
    image_page.go_to_media()
    time.sleep(2)
    image_page.go_to_images()
    time.sleep(2)
    image_page.add_new_image()
    time.sleep(2)
    image_page.import_from_url()
    time.sleep(2)
    image_page.enter_image_url(image_url)
    time.sleep(2)
    image_page.upload_image()
    time.sleep(2)
    image_page.enter_image_name(image_name)
    time.sleep(2)
    image_page.click_save()
    time.sleep(5)




