# Prueba_web.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_agregar_producto_al_carrito(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

    # obtener primer producto
    productos = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )
    primer_producto = productos[0]
    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

    # agregar al carrito
    boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")
    boton_agregar.click()

    # verificar que el contador aparezca
    badge = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert badge.text == "1", f"El contador del carrito muestra {badge.text} en lugar de 1"

    # ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

    # verificar producto en el carrito
    items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
    )
    assert len(items) == 1, "No se encontró el producto en el carrito"

    nombre_carrito = items[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre_producto == nombre_carrito, "El producto del carrito no coincide con el agregado"
