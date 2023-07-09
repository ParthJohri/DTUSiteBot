import os
import sys
import logging
import datetime
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
webdriver_service = Service(executable_path=r'/usr/bin/chromedriver')
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

log_file = datetime.datetime.now()
log_file = "./logs/" + str(log_file).replace(" ", "_").replace(".", "_").replace(":", "_") + ".log"
logging.basicConfig(filename=log_file, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

with open('credentials.txt') as file:
    username = file.readline().strip()
    password = file.readline().strip()

subject_list = []
with open('subjects.txt') as file:
    for subject in file.readlines():
        subject_list.append(subject.strip())

with open('parameters.txt') as file:
    website_loading_loop = int(file.readline().strip())
    subject_loading_loop = int(file.readline().strip())
    log_count = int(file.readline().strip())

for j in range(website_loading_loop):
    try:
        driver.get('https://cumsdtu.in/registration_student/login/login.jsp?courseRegistration')
        username_field = driver.find_element(By.XPATH, "//input[@name='userName']")
        username_field.send_keys(username)
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys(password)
        login_button = driver.find_element(By.XPATH, "//input[@value='Log In']")
        login_button.click()
        try:
            error = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/form/p[2]")
            if error:
                continue  # Restart the loop
        except:
            sleep(10)
            try:
                notification = driver.find_element(By.XPATH, "//*[contains(text(),' Course Registration is not open. Kindly visit later on.')]")
                logging.error('REG NOT OPEN')
                sleep(1)
            except:
                try:
                    subject_elements = []
                    wait = WebDriverWait(driver, 120)  # Maximum wait time in seconds
                    element_locator = (By.CSS_SELECTOR, "div.course.isDisabled")
                    wait.until(EC.visibility_of_element_located(element_locator))
                    save_button = driver.find_element(By.XPATH, "//button[@class='narrow mat-button mat-save']")
                    for subject in subject_list:
                        temp_element = driver.find_element(By.XPATH, "//*[contains(text(),'" + subject + " Cr:4.0')]")
                        subject_elements.append(temp_element)
                    for i in range(subject_loading_loop):
                        try:
                            if len(subject_elements) == 0:
                                quit()
                            for element in subject_elements:
                                element.click()
                                save_button.click()
                                sleep(0.6)
                        except:
                            logging.error("Error while registering subject.")
                except:
                    logging.error("Invalid subject codes. Try editing the subjects.txt file")
    except:
        logging.error("LOGIN ISSUE")
