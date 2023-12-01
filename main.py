# main_script.py
import logging
import datetime
from time import sleep
from modules.webdriver_utils import setup_driver
from modules.file_utils import read_credentials, read_subjects, read_parameters
from modules.registration_utils import login, check_login_error, check_registration_open, register_subjects

def configure_logging():
    log_file = datetime.datetime.now()
    log_file = f"./logs/{str(log_file).replace(' ', '_').replace('.', '_').replace(':', '_')}.log"
    logging.basicConfig(filename=log_file, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def main():
    configure_logging()
    driver = setup_driver()
    
    try:
        username, password = read_credentials()
        subject_list = read_subjects()
        website_loading_loop, subject_loading_loop, log_count = read_parameters()
        
        for j in range(website_loading_loop):
            try:
                login(driver, username, password)

                if check_login_error(driver):
                    continue  # Restart the loop

                if check_registration_open(driver):
                    continue  # Restart the loop

                register_subjects(driver, subject_list, subject_loading_loop)

            except:
                logging.error("LOGIN ISSUE")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
