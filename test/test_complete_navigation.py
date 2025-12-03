import pytest
from page.login_page import Login_Page
from page.inventory_page import Inventory_Page
from page.cart_page import Cart_Page
from page.checkout_page import CheckoutPage
from page.checkout_overview_page import CheckoutOverviewPage
import time

def test_complete_navegation(driver):
    login = Login_Page(driver)
    inventory = Inventory_Page(driver)
    cart = Cart_Page(driver)
    checkout = CheckoutPage(driver)
    overvierw = CheckoutOverviewPage(driver)

    # Logueo
    login.open()
    login.login("standard_user", "secret_sauce")
    time.sleep (4)
    # Ingreso en la pagina de inventario 
    assert inventory.is_at_page()
    # Seleciono producto y lo cargo al carrito
    inventory.add_product_to_cart(4)
    inventory.add_product_to_cart(2)
    inventory.add_product_to_cart(0)
    # Ingreso al carrito
    inventory.go_to_cart()
    # Ingreso en el checkout
    cart.go_to_checkout()
    time.sleep(4)
    # Completo la informacion requerida
    checkout.fill_customer_info("gracie","darling","6558")
    checkout.continue_to_overview()
    time.sleep (4)
    # en la pagina de overview
    overvierw.finish()
    # Verifico página de completado
    assert overvierw.is_at_page()
    assert "Thank you for your order!" in overvierw.get_success_message()
    assert overvierw.is_success_image_displayed()
    
    # Vuelvo al inicio
    overvierw.back_to_home()
    assert inventory.is_at_page()

