import pytest
from page.login_page import Login_Page
from page.inventory_page import Inventory_Page
from page.cart_page import Cart_Page
from page.checkout_page import CheckoutPage
import time

def test_checkout_process(driver):
    login = Login_Page(driver)
    inventory = Inventory_Page(driver)
    cart = Cart_Page(driver)
    checkout = CheckoutPage(driver)
    # inicio, logueo de la pagina 
    login.open()
    login.login("standard_user", "secret_sauce")
    time.sleep(4)
    # una vez ingresado, entro en la pagina inventary y seleciono un  producto
    inventory.add_product_to_cart(0)
    # ingreso en el carrito
    inventory.go_to_cart()
    time.sleep(4)
    # ingreso en el checkout
    cart.go_to_checkout()
    time.sleep(3)
    # verifico que ingrese en la pagina de checkout
    assert checkout.is_at_page()
    
    # Lleno la información requerida
    checkout.fill_customer_info("Barry", "Allen", "Flash_Run")
    checkout.continue_to_overview()
    # verifico que paso a la siguente pagina del proceso de checkout
    assert "checkout-step-two" in driver.current_url

def test_checkout_validation(driver):
    login = Login_Page(driver)
    inventory = Inventory_Page(driver)
    cart = Cart_Page(driver)
    checkout = CheckoutPage(driver)
    
    # inicio, logueo de la pagina 
    login.open()
    login.login("standard_user", "secret_sauce")

    time.sleep(4)
    
    # una vez ingresado, entro en la pagina inventary y seleciono un  producto
    inventory.add_product_to_cart(0)
    # ingreso en el carrito
    inventory.go_to_cart()
    # ingreso en el checkout
    cart.go_to_checkout()
    
    # Intentio continuar sin información
    checkout.continue_to_overview()
    # verifico el mensaje de error
    error_message = checkout.get_error_message()
    assert "First Name is required" in error_message