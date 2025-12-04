import pytest
from page.login_page import Login_Page
from page.inventory_page import Inventory_Page
from data.data_login import CASOS_LOGIN
from utils.helpers import get_login_csv
from test.conftest import logger

@pytest.mark.parametrize("username,password,login_bool",get_login_csv())
def test_login(driver, username, password, login_bool):
    logger.info("\n=== Test Login: login de users ===")
    print("\n=== Test_login: login de users ===")
    #crear objeto
    loginpage = Login_Page(driver)
    inventory = Inventory_Page(driver)
    loginpage.open()
    driver.save_screenshot('screenshot/test_login/login.png')
    loginpage.login(username,password)
    
    
    if login_bool == True:
        logger.info("logueo correcto - OK")
        print("✅ logueo correcto - OK")
        driver.save_screenshot('screenshot/test_login/login_ok.png')
        assert inventory.is_at_page()
    else:
        logger.info("mesage de error:"+ loginpage.get_error_message())
        print("mesage de error:"+loginpage.get_error_message())
        logger.info("logueo incorrecto - OK")
        print("✅ logueo incorrecto - OK")
        driver.save_screenshot('screenshot/test_login/login_fail.png')
        assert loginpage.is_at_page()