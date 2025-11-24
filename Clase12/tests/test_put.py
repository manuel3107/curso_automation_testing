import requests
import time
import pytest

@pytest.mark.api
def test_put_users(url_base,header_request):
    url = f"{url_base}/2"

    data = {"name":"Valentina","job":"Tutora"}

    inicio = time.time()
    response = requests.put(url,headers=header_request,json=data)
    tiempo_diff = time.time() - inicio
    
     
    # Validacion de status
    assert response.status_code == 200

    # Validacion de tiempo de respuesta
    assert tiempo_diff < 2, f"La api tardo demasiado {tiempo_diff}"

    # Validacion de datos
    body = response.json()

    assert "updatedAt" in body
    assert isinstance(body["name"],str)

    assert body["name"] == data["name"]

