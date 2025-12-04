from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import URL_page 
from selenium.webdriver.common.by import By



class Login_Page:
    login_name_box = (By.NAME,"user-name")
    login_password_box = (By.NAME,"password")
    login_button = (By.ID,"login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR,'h3[data-test="error"]')
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(URL_page)

    def is_at_page( self ):
        return URL_page in self.driver.current_url

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
    
    def this_error_is_visible(self):
        # Comprueba si aparece un mensaje de error 
        # en la página tras un intento de login fallido.
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self._ERROR_MESSAGE)) 
            return True 
        except: 
            return False

    def get_error_message(self):
        #Obtiene el texto del mensaje de error.
        if self.this_error_is_visible():
            return self.driver.find_element(*self._ERROR_MESSAGE).text 
        return ""   