# tests/test_carrito.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.actions import login, agregar_primer_producto

@pytest.mark.usefixtures("driver")
def test_agregar_producto_al_carrito(driver):
    """Agregar el primer producto al carrito y verificar contador."""
    login(driver)
    nombre, precio = agregar_primer_producto(driver)

    # Verificar que el contador se incrementó
    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert badge.text == "1", "El contador del carrito no se incrementó correctamente."

    # Validar que el ítem aparece en el carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

    nombre_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert nombre_carrito == nombre, f"Nombre distinto: {nombre_carrito} vs {nombre}"
    assert precio_carrito == precio, f"Precio distinto: {precio_carrito} vs {precio}"
