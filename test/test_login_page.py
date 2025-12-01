import pytest
from page.login_page import Login_Page
from data.data_login import CASOS_LOGIN
from utils.helpers import get_login_csv

@pytest.mark.parametrize("username,password,login_bool",get_login_csv())
def test_login(driver, username, password, login_bool):
    #crear objeto
    loginpage = Login_Page(driver)
    loginpage.open()
    loginpage.login(username,password)
    print(loginpage.get_error_message())

    if login_bool:
        assert "inventory.html"
    else:
        assert "inventory.html"