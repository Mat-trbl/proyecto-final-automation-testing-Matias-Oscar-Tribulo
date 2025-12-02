from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import URL_page 
from selenium.webdriver.common.by import By

class Cart_Page:

    URL_CURRENT = "https://www.saucedemo.com/cart.html"
    CART_ITEMS = (By.CLASS_NAME, 'cart_item')
    CART_COUNTER = (By.CLASS_NAME,'shopping_cart_badge')
    CONTINUE_SHOPPING_BUTTON = (By.ID, 'continue-shopping')
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    REMOVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Remove')]")
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    
    def __init__(self,driver):
        self.driver = driver

    def is_at_page(self):
        return self.URL_CURRENT in self.driver.current_url
    
    def get_cart_product(self):
        return self.driver.find_elements(*self.CART_ITEMS)
    
    def get_products_name(self):
        product_name = self.driver.find_elements(*self.CART_ITEMS)
        return [product.text for product in product_name]
    
    def continue_shopping(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BUTTON)).click()

    def go_to_checkout(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()

    def get_cart_items_count(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)

    def remove_item(self, item_index):
        remove_buttons = self.driver.find_elements(*self.REMOVE_BUTTON)
        if remove_buttons and item_index < len(remove_buttons):
            remove_buttons[item_index].click()

    def get_cart_badge_count(self):
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except:
            return 0

