from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username="standard_user", password="secret_sauce"):
    driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Esperar que cargue la página de inventario
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
    assert "inventory" in driver.current_url, "El login no redirigió correctamente."
    assert "Swag Labs" in driver.title, "El título no contiene 'Swag Labs'."
    return driver

def agregar_primer_producto(driver):
    # Esperar que los productos aparezcan
    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No hay productos en la página."
    primer_producto = productos[0]

    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

    boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")
    boton_agregar.click()

    return nombre, precio