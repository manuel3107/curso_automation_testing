import requests
import pytest

@pytest.mark.api
def test_patch_users(url_base,header_request):
    url = f"{url_base}/2"

    data = {"name":"Jose"}

    response = requests.patch(url,headers=header_request,json=data)

    # Validacion status code
    assert response.status_code == 200

    # Validacion de datos
    body = response.json()
    
    assert body["name"] == data["name"]