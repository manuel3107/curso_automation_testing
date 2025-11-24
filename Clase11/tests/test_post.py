import requests
import pytest

@pytest.mark.api
def test_post_users(url_base, header_request):
    url = f"{url_base}"
    payload = {"name":"Jose","job":"Profesor"}

    response = requests.post(url,headers=header_request,json=payload)

    # VERIFICAR QUE EL RECURSO SE HAYA CREADO
    assert response.status_code == 201

    data = response.json()

    # VERIFICAR QUE EL NOMBRE DE LA RESPUESTA SEA EL MISMO QUE EL ENVIADO
    assert data["name"] == payload["name"]

    # VERIFICAR QUE LA RESPUESTA TENGA UN ID
    assert "id" in data


