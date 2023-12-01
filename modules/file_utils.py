# file_utils.py

def read_credentials(filename='new_credentials.txt'):
    with open(filename) as file:
        username = file.readline().strip()
        password = file.readline().strip()
    return username, password

def read_subjects(filename='new_subjects.txt'):
    subject_list = []
    with open(filename) as file:
        for subject in file.readlines():
            subject_list.append(subject.strip())
    return subject_list

def read_parameters(filename='new_parameters.txt'):
    with open(filename) as file:
        website_loading_loop = int(file.readline().strip())
        subject_loading_loop = int(file.readline().strip())
        log_count = int(file.readline().strip())
    return website_loading_loop, subject_loading_loop, log_count
