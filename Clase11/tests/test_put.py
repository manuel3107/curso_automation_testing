import requests
import time
import pytest

@pytest.mark.api
def test_put_request(user_url,header_request):
    url = f"{user_url}/1"
    
    data = {"name": "Valentina", "job": "tutora"}
    inicio = time.time()
    response = requests.put(url, headers=header_request, json=data)
    tiempo_diff = time.time() - inicio
    
    #validacion status
    assert response.status_code == 200
    
    