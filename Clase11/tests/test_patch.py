import requests
import pytest

@pytest.mark.api
def test_patch_request(header_request, user_url):
    url = f"{user_url}/2"
    

    data = {"name": "Jose"}

    response = requests.patch(url, headers=header_request, json=data)

    #validacion status code
    assert response.status_code == 200
    
    #validacion de datos actualizados
    body = response.json()
    assert body["name"] == data["name"]

