import pytest
from page.login_page import Login_Page
from page.inventory_page import Inventory_Page
from page.cart_page import Cart_Page
from page.checkout_page import CheckoutPage
from test.conftest import logger
import time

def test_checkout_process(driver):
    logger.info("\n=== Test checkout process: checkout page management  ===")
    print("\n=== Test_checkout_process: checkout page management  ===")
    login = Login_Page(driver)
    inventory = Inventory_Page(driver)
    cart = Cart_Page(driver)
    checkout = CheckoutPage(driver)
    # Inicio, logueo de la pagina 
    login.open()
    driver.save_screenshot('screenshot/test_checkout/login.png')
    login.login("standard_user", "secret_sauce")
    time.sleep(4)
    logger.info("correct login - OK")
    print("✅ correct login - OK")
    # Una vez ingresado, entro en la pagina inventary y seleciono un  producto
    driver.save_screenshot('screenshot/test_checkout/inventory.png')
    inventory.add_product_to_cart(0)
    driver.save_screenshot('screenshot/test_checkout/add_product.png')
    logger.info("correct product loading - OK")
    print("✅ correct product loading - OK")
    # Ingreso en el carrito
    inventory.go_to_cart()
    driver.save_screenshot('screenshot/test_checkout/cart.png')
    time.sleep(4)
    logger.info("correct cart entering - OK")
    print("✅ correct cart entering - OK")
    # Ingreso en el checkout
    cart.go_to_checkout()
    driver.save_screenshot('screenshot/test_checkout/checkout.png')
    time.sleep(3)
    # Verifico que ingrese en la pagina de checkout
    assert checkout.is_at_page()
    logger.info("correct checkout entering - OK")
    print("✅ correct checkout entering - OK")
    # Lleno la información requerida
    checkout.fill_customer_info("Barry", "Allen", "1852")
    driver.save_screenshot('screenshot/test_checkout/info_checkout.png')
    checkout.continue_to_overview()
    driver.save_screenshot('screenshot/test_checkout/overview.png')
    # verifico que paso a la siguente pagina del proceso de checkout
    assert "checkout-step-two" in driver.current_url
    logger.info("correct info loading - OK")
    print("✅ correct info loadring - OK")

def test_checkout_validation(driver):
    logger.info("\n=== Test checkout validation: checkout page management  ===")
    print("\n=== Test_checkout_validation: checkout page management  ===")
    login = Login_Page(driver)
    inventory = Inventory_Page(driver)
    cart = Cart_Page(driver)
    checkout = CheckoutPage(driver)
    
    # inicio, logueo de la pagina 
    login.open()
    login.login("standard_user", "secret_sauce")

    time.sleep(4)
    logger.info("correct login - OK")
    print("✅ correct login - OK")
    # una vez ingresado, entro en la pagina inventary y seleciono un  producto
    inventory.add_product_to_cart(0)
    logger.info("correct product loading - OK")
    print("✅ correct product loading - OK")
    # ingreso en el carrito
    inventory.go_to_cart()
    logger.info("correct cart entering - OK")
    print("✅ correct cart entering - OK")
    # ingreso en el checkout
    cart.go_to_checkout()
    logger.info("correct checkout entering - OK")
    print("✅ correct checkout entering - OK")
    
    # Intentio continuar sin información
    checkout.continue_to_overview()
    # verifico el mensaje de error
    driver.save_screenshot('screenshot/test_checkout/error_message_checkout.png')
    error_message = checkout.get_error_message()
    logger.info(error_message)
    print(error_message)   
    assert "First Name is required" in error_message
    logger.info("message error - OK")
    print("✅ message error - OK")