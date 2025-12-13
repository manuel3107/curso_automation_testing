import os

BASE_URL_UI = "https://www.saucedemo.com"
BASE_URL_API = "https://reqres.in/api"

BROWSER = "chrome"
HEADLESS = False

EXPLICIT_WAIT = 10

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(PROJECT_ROOT, "data")
REPORTS_PATH = os.path.join(PROJECT_ROOT, "reports")
SCREENSHOTS_PATH = os.path.join(PROJECT_ROOT, "screenshots")
LOG_PATH = os.path.join(REPORTS_PATH, "execution.log")

