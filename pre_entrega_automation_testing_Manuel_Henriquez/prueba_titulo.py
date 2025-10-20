# Prueba_titulo.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_verificar_titulo_y_productos(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

    # validar título
    titulo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    ).text
    assert "Products" in titulo or "Swag" in driver.title, "El título no coincide"

    # verificar productos visibles
    productos = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )
    assert len(productos) > 0, "No se encontraron productos en el inventario"

    # mostrar nombre y precio del primer producto
    nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"Primer producto: {nombre} - Precio: {precio}")
    assert nombre and precio
