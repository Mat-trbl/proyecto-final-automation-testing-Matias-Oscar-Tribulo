from page.login_page import Login_Page
from page.inventory_page import Inventory_Page
from test.conftest import logger
import time

tittle_inventory = "Products"

def test_inventory( driver ):
    logger.info("\n=== Test inventory: inventory page management  ===")
    print("\n=== Test_inventory: inventory page management  ===")
    login = Login_Page(driver)
    inventory = Inventory_Page(driver)

    login.open()
    driver.save_screenshot('screenshot/test_inventory/login.png')
    login.login("standard_user", "secret_sauce")
    time.sleep(5)

    assert inventory.is_at_page()
    logger.info("correct login - OK")
    print("✅ correct login - OK")
    assert inventory.get_title() == tittle_inventory
    logger.info("page title - OK")
    print("✅ page title - OK")
    driver.save_screenshot('screenshot/test_inventory/inventory.png')
    print("\n"+inventory.get_title())
    inventory.add_product_to_cart(1)
    print("\n Numeros de productos en el carrito: \t"+ str(inventory.get_cart_counter()))
    inventory.add_product_to_cart(4)
    inventory.add_product_to_cart(2)
    print("\n Numeros de productos en el carrito: \t"+ str(inventory.get_cart_counter()))
    assert inventory.get_cart_counter() == 3
    logger.info("correct product loading - OK")
    print("✅ correct product loading - OK")
    driver.save_screenshot('screenshot/test_inventory/select_products.png')
    inventory.go_to_cart()
    driver.save_screenshot('screenshot/test_inventory/cart.png')
    logger.info("correct cart entering - OK")
    print("✅ correct cart entering - OK")
    inventory.logout()
    time.sleep(4)
    assert "https://www.saucedemo.com/" in driver.current_url
    logger.info("correct cart logouting - OK")
    print("✅ correct cart logouting - OK")