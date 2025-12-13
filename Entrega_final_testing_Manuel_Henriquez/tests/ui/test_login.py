from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_reader import read_json
from utils.logger import get_logger

logger = get_logger("TestLogin")
data = read_json("login_data.json")

def test_login_success(driver):
    logger.info("Inicio test_login_success")
    login = LoginPage(driver)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )

    inventory = InventoryPage(driver)
    assert "inventory" in driver.current_url
    logger.info("Login exitoso validado")

def test_login_invalid(driver):
    logger.info("Inicio test_login_invalid")
    login = LoginPage(driver)
    login.login(
        data["invalid_user"]["username"],
        data["invalid_user"]["password"]
    )

    assert "Epic sadface" in login.get_error_message()
    logger.info("Mensaje de error validado correctamente")

