from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
#espera implicita
driver.implicitly_wait(5)

#espera explicita
wait = WebDriverWait(driver, 10)

driver.get("https://www.saucedemo.com/")


#Localizacion e interaccion de elementos

wait.until(EC.presence_of_element_located((By.ID, "user-name")))
usuario = driver.find_element(By.ID, "user-name")

wait.until(EC.visibility_of_element_located((By.ID, "password")))
contraseña = driver.find_element(By.ID, "password")

wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
boton_login = driver.find_element(By.ID, "login-button")

usuario.send_keys("standard_user")
contraseña.send_keys("secret_sauce")
boton_login.click()