import pytest
import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from utils.config import (
    BASE_URL_UI,
    SCREENSHOTS_PATH,
    HEADLESS
)

@pytest.fixture
def driver(request):
    chrome_options = Options()

    if HEADLESS:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.maximize_window()
    driver.get(BASE_URL_UI)

    yield driver

    if request.node.rep_call.failed:
        os.makedirs(SCREENSHOTS_PATH, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name
        screenshot_path = os.path.join(
            SCREENSHOTS_PATH,
            f"{test_name}_{timestamp}.png"
        )

        driver.save_screenshot(screenshot_path)

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
