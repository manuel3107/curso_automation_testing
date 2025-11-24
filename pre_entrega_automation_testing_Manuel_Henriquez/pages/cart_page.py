from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class cartPage:
    
    _CART_ITEMS = (By.CLASS_NAME, "CART_ITEM")
    _ITEMS_NAMES = (By.CLASS_NAME, "inventory_item_name")
    _CHECKOUT_BUTTON = (By.ID, "checkout")
    _CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    
    def __init__(self,driver):
        self.driver = driver 
        self.wait = WebDriverWait(driver,10)
        self.wait.until(EC.url_contains("cart.html"))
        
    def obtener_productos_en_carrito(self):
        return self.driver.find_elements(*self._CART_ITEMS)
    
    def obtener_nombres_productos(self):
        elementos_nombres = self.driver.find_elements(*self._ITEMS_NAMES)
        return [elemento.text for elemento in elementos_nombres]
    
    def continuar_comparando(self):
        self.driver.find_element(*self._CONTINUE_SHOPPING_BUTTON).click()
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)
    
    def productos_checkout(self):
        self.driver.find_element(*self._CHECKOUT_BUTTON).click()
        return self