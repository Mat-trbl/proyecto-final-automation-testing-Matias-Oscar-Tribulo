from page.login_page import Login_Page
from page.inventory_page import Inventory_Page
from page.cart_page import Cart_Page
from test.conftest import logger
import time

def test_cart(driver):
    logger.info("\n=== Test cart: cart page management  ===")
    print("\n=== Test_cart: cart page management  ===")
    login = Login_Page(driver)
    inventory = Inventory_Page(driver)
    cart = Cart_Page(driver)

    # inicio, logueo de la pagina 
    login.open()
    driver.save_screenshot('screenshot/test_cart/login.png')
    login.login("standard_user", "secret_sauce")
    driver.save_screenshot('screenshot/test_cart/inventory.png')
    logger.info("correct login - OK")
    print("✅ correct login - OK")
    time.sleep(5)

    # una vez ingresado, entro en la pagina inventary y seleciono los productos
    inventory.add_product_to_cart(5)
    time.sleep(5)
    inventory.add_product_to_cart(2)
    time.sleep(5)
    inventory.add_product_to_cart(1)
    time.sleep(5)
    # ingreso al carrito
    inventory.go_to_cart()
    logger.info("correct cart entering - OK")
    print("✅ correct cart entering - OK")
    driver.save_screenshot('screenshot/test_cart/cart.png')
    # compruebo que estoy en la pagina del carrito
    assert cart.is_at_page()
    # verifico los productos en el carrito
    products = cart.get_products_name()
    lista_formateada = "\n".join(products)
    print("\n--- Productos Encontrados ---")
    print(lista_formateada)
    print("-----------------------------\n")
    # verifico la cantidad de producto en el carrito concuerda con 
    # los producto cargados y el valor del contador del carrito 
    assert len(products) == 3
    assert cart.get_cart_badge_count() == 3
    logger.info("correct product loading - OK")
    print("✅ correct product loading - OK")
    # remuevo un producto
    cart.remove_item(1)
    driver.save_screenshot('screenshot/test_cart/remove_producto.png')
    time.sleep(5)
    # verifico que la cantidad de producto restante concuerde y que el contador del carrito tambien
    assert cart.get_cart_items_count() == 2
    assert cart.get_cart_badge_count() == 2
    logger.info("correct product removing - OK")
    print("✅ correct product removing - OK")










