from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

# required for selenium to work
NODE_URL = "http://192.168.0.111:4444/wd/hub"
DOWNLOAD_PATH = os.path.join("home", "seluser", "Downloads")

prefs = {
    "download.default_directory": DOWNLOAD_PATH,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
}


def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--test-type")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920x1080")
    options.add_experimental_option("prefs", prefs)

    options.add_argument("--proxy-server=socks5://localhost:8157")
    options.add_argument("--ignore-ssl-errors=yes")
    options.add_argument("--ignore-certificate-errors")
    # browser setup
    driver = webdriver.Remote(
        desired_capabilities=options.to_capabilities(), command_executor=NODE_URL
    )
    driver.maximize_window()
    print("Driver initialized")
    driver.set_page_load_timeout(480)
    return driver
