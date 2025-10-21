# tests/test_inventario.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.actions import login

@pytest.mark.usefixtures("driver")
def test_titulo_inventario(driver):
    """Validar que el título 'Products' esté presente tras el login."""
    login(driver)
    titulo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    ).text
    assert titulo == "Products", f"Título incorrecto: {titulo}"

@pytest.mark.usefixtures("driver")
def test_presencia_de_productos(driver):
    """Comprobar que haya al menos un producto visible en la página."""
    login(driver)
    productos = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )
    assert len(productos) > 0, "No se encontraron productos visibles."

@pytest.mark.usefixtures("driver")
def test_menu_y_filtros_visibles(driver):
    """Validar que existan elementos importantes de la interfaz (menú y filtro)."""
    login(driver)
    menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "react-burger-menu-btn"))
    )
    filtro = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
    )
    assert menu.is_displayed(), "El menú no está visible."
    assert filtro.is_displayed(), "El filtro de productos no está visible."
