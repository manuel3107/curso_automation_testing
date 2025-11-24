from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InventoryPage:
    
    _TITLE_INVENTORY = (By.CLASS_NAME, "title")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _ADD_BUTTON = (By.CLASS_NAME, "btn_inventory")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")


    def __init__(self,driver):
        self.driver = driver 
        self.wait = WebDriverWait(driver,10)

    def obtener_titulo_inventario(self):
        return self.driver.find_element(*self._TITLE_INVENTORY).text
    
    def obtener_productos(self):
        return self.driver.find_elements(*self._PRODUCTS)
    
    def agergar_primer_producto(self):
        primer_boton = self.driver.find_elements(*self._ADD_BUTTON)[0]
        primer_boton.click()
        return self
    
    def obtener_contador_carrito(self):
        try:
            badge: self.driver.find_element(*self._CART_BADGE)
            return int(badge.text)
        except:
            return 0
    def ir_a_carrito(self):
        self.driver.find_element(*self._CART_LINK).click()
        from pages.cart_page import CartPage
        return CartPage(self.driver)
    
    def hacer_logout(self):
        self.driver.find_element(*self._MENU_BUTTON).click()
        logout_link = self.wait.until(EC.visibility_of_element_located(self._LOGOUT_LINK))
        from pages.login_page import LoginPage
        return LoginPage(self.driver) 
        
    
    