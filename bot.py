from csv import DictReader

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from settings import EMPLOYEE_REGISTER_PASSWORD, EMPLOYEE_REGISTER_USERNAME


def create_webdriver():
    return webdriver.Chrome("/usr/bin/chromedriver")


def connect(driver):
    driver.get("localhost:8000")


def login(driver):
    username_input = driver.find_element(By.ID, "id_username")
    password_input = driver.find_element(By.ID, "id_password")

    username_input.clear()
    username_input.send_keys(EMPLOYEE_REGISTER_USERNAME)

    password_input.clear()
    password_input.send_keys(EMPLOYEE_REGISTER_PASSWORD)

    button = driver.find_element(By.TAG_NAME, "button")
    button.click()


def access_employee_register_page(driver):
    dropdown = driver.find_element(By.ID, "navbarDropdown")
    dropdown.click()

    employee_register_opt = driver.find_element(
        By.LINK_TEXT, "Cadastrar Funcionário"
    )
    employee_register_opt.click()


def register_employee(driver, data):
    first_name_input = driver.find_element(By.ID, "id_first_name")
    first_name_input.clear()
    first_name_input.send_keys(data["first_name"])

    last_name_input = driver.find_element(By.ID, "id_last_name")
    last_name_input.clear()
    last_name_input.send_keys(data["last_name"])

    role_input = driver.find_element(By.ID, "id_role")
    role_input.clear()
    role_input.send_keys(data["role"])

    email_input = driver.find_element(By.ID, "id_email")
    email_input.clear()
    email_input.send_keys(data["email"])

    username_input = driver.find_element(By.ID, "id_username")
    username_input.clear()
    username_input.send_keys(data["username"])

    password_input = driver.find_element(By.ID, "id_password")
    password_input.clear()
    password_input.send_keys(data["password"])

    driver.find_element(By.CLASS_NAME, "fa-plus").click()


def main():
    driver = create_webdriver()
    connect(driver)
    login(driver)
    access_employee_register_page(driver)

    with open("employees.csv", "r") as file:
        csv_dict_reader = DictReader(file)
        for data in csv_dict_reader:
            register_employee(driver, data)


if __name__ == "__main__":
    main()
