from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger
from utils.config import EXPLICIT_WAIT

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)
        self.logger = get_logger(self.__class__.__name__)

    def click(self, locator):
        self.logger.info(f"Haciendo click en {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        self.logger.info(f"Escribiendo texto en {locator}")
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        self.logger.info(f"Obteniendo texto de {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator)).text

