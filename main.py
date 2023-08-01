from process import initialize_driver
from birth_verification import birth_verfication

everify = "https://everify.bdris.gov.bd/"

if __name__ == "__main__":
    try:
        driver = initialize_driver()  # initialize driver
        birth_verification = birth_verfication(driver, everify)
        driver.close()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        driver.close()
