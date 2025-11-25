from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import URL_page 
from selenium.webdriver.common.by import By


class Login_Page:
    login_name_box = (By.NAME,"user-name")
    login_password_box = (By.NAME,"password")
    login_button =(By.ID,"login-button")
    
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(URL_page)

    def login(self, username, password):
        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self.login_name_box)
        ).send_keys(username)
        WebDriverWait(self.driver,54).until(
            EC.element_to_be_clickable(self.login_password_box)
        ).send_keys(password)
        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()