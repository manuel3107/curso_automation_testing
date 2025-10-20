# test_login.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_exitoso(driver):
    driver.get("https://www.saucedemo.com/")

    # completar formulario
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # esperar redirección
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url, "No se redirigió correctamente al inventario"

    # validar título o nombre de página
    titulo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    ).text
    assert "Products" in titulo or "Swag Labs" in driver.title
