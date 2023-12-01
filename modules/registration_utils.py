# registration_utils.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import logging

def login(driver, username, password):
    driver.get('https://cumsdtu.in/registration_student/login/login.jsp?courseRegistration')
    username_field = driver.find_element(By.XPATH, "//input[@name='userName']")
    username_field.send_keys(username)
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    password_field.send_keys(password)
    login_button = driver.find_element(By.XPATH, "//input[@value='Log In']")
    login_button.click()

def check_login_error(driver):
    try:
        error = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/form/p[2]")
        if error:
            return True
    except:
        return False

def check_registration_open(driver):
    try:
        notification = driver.find_element(By.XPATH, "//*[contains(text(),' Course Registration is not open. Kindly visit later on.')]")
        logging.error('REG NOT OPEN')
        sleep(1)
        return True
    except:
        return False

def register_subjects(driver, subject_list, subject_loading_loop):
    subject_elements = []
    wait = WebDriverWait(driver, 120)  # Maximum wait time in seconds
    element_locator = (By.CSS_SELECTOR, "div.course.isDisabled")
    wait.until(EC.visibility_of_element_located(element_locator))
    save_button = driver.find_element(By.XPATH, "//button[@class='narrow mat-button mat-save']")
    
    for subject in subject_list:
        temp_element = driver.find_element(By.XPATH, f"//*[contains(text(),'{subject} Cr:4.0')]")
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
