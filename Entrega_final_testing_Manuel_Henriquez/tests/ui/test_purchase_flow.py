from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_reader import read_json
from utils.logger import get_logger

logger = get_logger("TestPurchaseFlow")
data = read_json("login_data.json")

def test_add_product_to_cart(driver):
    logger.info("Inicio flujo de compra")

    LoginPage(driver).login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )

    inventory = InventoryPage(driver)
    inventory.add_product_to_cart()
    inventory.go_to_cart()

    assert "cart" in driver.current_url
    logger.info("Producto agregado al carrito correctamente")

