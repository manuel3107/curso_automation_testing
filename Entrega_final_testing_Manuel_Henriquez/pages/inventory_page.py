from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self):
        self.logger.info("Agregando producto al carrito")
        self.click(self.ADD_TO_CART)

    def go_to_cart(self):
        self.logger.info("Navegando al carrito")
        self.click(self.CART_ICON)

