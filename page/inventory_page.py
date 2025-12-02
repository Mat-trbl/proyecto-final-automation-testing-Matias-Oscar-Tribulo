from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
import time

class Inventory_Page:
    URL_CURRENT = 'https://www.saucedemo.com/inventory.html'
    MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    LOGOUT_LINK_BUTTON = (By.ID, 'logout_sidebar_link')
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')
    TITLE =(By.CLASS_NAME, 'title')
    CART_COUNTER = (By.CLASS_NAME,'shopping_cart_badge')
    def __init__(self , driver):
        self.driver = driver

    def is_at_page( self ):
        return self.URL_CURRENT in self.driver.current_url
    
    def get_title(self):
        return self.driver.find_element(*self.TITLE).text

    
    def add_product_to_cart(self, product_index):
        add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        if add_buttons and product_index < len(add_buttons):
            add_buttons[product_index].click()

    def get_cart_counter(self): 
        #Obtiene el número de productos en el carrito.
        try:
            badge = self.driver.find_element(*self.CART_COUNTER) 
            return int(badge.text) 
        except: 
            return 0
    
    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()
    
    def logout( self ):
        self.driver.find_element(*self.MENU_BUTTON).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGOUT_LINK_BUTTON)
        ).click()
