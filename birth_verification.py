from selenium.webdriver.common.keys import Keys
from time import sleep

# Xpath for birth verification
BIRTH_REGISTRATION_NO = '//*[@id="ubrn"]'
DATE_OF_BIRTH = '//*[@id="BirthDate"]'
CAPTCHA = '//*[@id="CaptchaInputText"]'

# some dummy values
birth_reg = 12345678901234567
user_dob = "1998-12-25"
captch_input = "10"
BIRTH_URL = "https://everify.bdris.gov.bd/"


def birth_verfication(driver, url):
    driver.get(BIRTH_URL)

    registration_no = driver.find_element("xpath", BIRTH_REGISTRATION_NO).send_keys(
        birth_reg, Keys.DOWN
    )
    dob = driver.find_element("xpath", DATE_OF_BIRTH).send_keys(user_dob, Keys.DOWN)
    captch = driver.find_element("xpath", CAPTCHA).send_keys(captch_input, Keys.DOWN)
    for i in range(10):
        print("Birth verification is running...")
        sleep(1)

    return driver
