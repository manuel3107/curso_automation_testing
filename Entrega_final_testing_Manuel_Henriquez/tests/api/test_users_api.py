import requests
from utils.config import BASE_URL_API
from utils.logger import get_logger

logger = get_logger("TestAPI")

def test_get_users():
    logger.info("GET /users")
    response = requests.get(f"{BASE_URL_API}/users?page=2")
    assert response.status_code == 200
    assert len(response.json()["data"]) > 0

def test_create_user():
    logger.info("POST /users")
    payload = {"name": "Manuel", "job": "QA"}
    response = requests.post(f"{BASE_URL_API}/users", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Manuel"

def test_delete_user():
    logger.info("DELETE /users/2")
    response = requests.delete(f"{BASE_URL_API}/users/2")
    assert response.status_code == 204

