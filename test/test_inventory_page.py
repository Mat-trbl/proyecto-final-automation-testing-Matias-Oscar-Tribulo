from page.login_page import Login_Page
from page.inventory_page import Inventory_Page
import time
tittle_inventary = "Products"
def test_inventory( driver ):
    login = Login_Page(driver)
    inventory = Inventory_Page(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    time.sleep(5)

    assert inventory.is_at_page()
    assert inventory.get_title() == tittle_inventary
    print("\n"+inventory.get_title())
    inventory.add_product_to_cart(1)
    print("\n Numeros de productos en el carrito: \t"+ str(inventory.get_cart_counter()))
    inventory.add_product_to_cart(4)
    inventory.add_product_to_cart(2)
    print("\n Numeros de productos en el carrito: \t"+ str(inventory.get_cart_counter()))
    assert inventory.get_cart_counter() == 3
    inventory.go_to_cart()
    inventory.logout()
    time.sleep(4)
    assert "https://www.saucedemo.com/" in driver.current_url