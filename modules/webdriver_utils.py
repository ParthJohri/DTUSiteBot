# webdriver_utils.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    webdriver_service = Service(executable_path=r'/usr/bin/chromedriver')
    return webdriver.Chrome(service=webdriver_service, options=chrome_options)
