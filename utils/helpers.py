from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located as EC_presence

import os
import csv
import json
from pathlib import Path

URL_page = 'https://www.saucedemo.com/'

def get_driver():

    chrome_options = Options()

    #Instalacion del driver
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    #time.sleep(2)
    driver.implicitly_wait(5)
    return(driver)

def get_file_path(file_name,folder="data"):
    #ruta relativa
    current_file =os.path.dirname(__file__) #el archivo donde me encuentro
    file_path =os.path.join(current_file,"..",folder,file_name)
    #../data/data_login.csv => rel
    return os.path.abspath(file_path)

def get_login_csv(csv_file="data_login.csv"):
    #csv_file = get_file_path(csv_file, "data")

    csv_file = Path(__file__).parent.parent / "data" / csv_file
    #../data/data_login.csv
    casos = []

    with open(csv_file, newline="" ) as h:
        read = csv.DictReader(h)

        for i in read:
            username = i["username"]
            password = i["password"]
            login_example_str = i["login_example"]
            # combierto a boleano
            login_example = login_example_str.lower() == "true"
            casos.append((username,password,login_example))
    return casos
