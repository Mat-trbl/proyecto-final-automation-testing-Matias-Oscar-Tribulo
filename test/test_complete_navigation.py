import pytest
from page.login_page import Login_Page
from page.inventory_page import Inventory_Page
from page.cart_page import Cart_Page
from page.checkout_page import CheckoutPage
from page.checkout_overview_page import CheckoutOverviewPage
from test.conftest import logger
import time

def test_complete_navegation(driver):
    logger.info("\n=== Test complete navigation: checkout page management  ===")
    print("\n=== Test_complete_navigation: checkout page management  ===")
    login = Login_Page(driver)
    inventory = Inventory_Page(driver)
    cart = Cart_Page(driver)
    checkout = CheckoutPage(driver)
    overvierw = CheckoutOverviewPage(driver)

    # Logueo
    login.open()
    driver.save_screenshot('screenshot/test_complete_navigation/login.png')
    login.login("standard_user", "secret_sauce")
    driver.save_screenshot('screenshot/test_complete_navigation/inventory.png')
    time.sleep (4)
    # Ingreso en la pagina de inventario 
    assert inventory.is_at_page()
    logger.info("correct login - OK")
    print("✅ correct login - OK")
    # Seleciono producto y lo cargo al carrito
    inventory.add_product_to_cart(4)
    inventory.add_product_to_cart(2)
    inventory.add_product_to_cart(0)
    driver.save_screenshot('screenshot/test_complete_navigation/add_product.png')
    logger.info("correct product loading - OK")
    print("✅ correct product loading - OK")
    # Ingreso al carrito
    inventory.go_to_cart()
    driver.save_screenshot('screenshot/test_complete_navigation/cart.png')
    logger.info("correct cart entering - OK")
    print("✅ correct cart entering - OK")
    # Ingreso en el checkout
    cart.go_to_checkout()
    driver.save_screenshot('screenshot/test_complete_navigation/checkout.png')
    time.sleep(4)
    logger.info("correct checkout entering - OK")
    print("✅ correct checkout entering - OK")
    # Completo la informacion requerida
    checkout.fill_customer_info("gracie","darling","6558")
    driver.save_screenshot('screenshot/test_complete_navigation/add_info.png')
    checkout.continue_to_overview()
    time.sleep (4)
    driver.save_screenshot('screenshot/test_complete_navigation/overview.png')
    logger.info("correct info loading - OK")
    print("✅ correct info loadring - OK")
    # en la pagina de overview
    overvierw.finish()
    # Verifico página de completado
    assert overvierw.is_at_page()
    logger.info("successful completion of purchase - OK")
    print("✅ successful completion of purchase - OK")
    assert "Thank you for your order!" in overvierw.get_success_message()
    driver.save_screenshot('screenshot/test_complete_navigation/message_finish.png')
    assert overvierw.is_success_image_displayed()
    logger.info("message:"+ overvierw.get_success_message() + " - OK")
    print("✅message:"+ overvierw.get_success_message() + " - OK")
    # Vuelvo al inicio
    overvierw.back_to_home()
    assert inventory.is_at_page()
    logger.info("correct back at home - OK")
    print("✅ correct back at home - OK")

