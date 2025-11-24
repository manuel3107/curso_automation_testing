import requests
import pytest

@pytest.mark.api
def test_delete_users(url_base,header_request):
    url = f"{url_base}/2"

    response = requests.delete(url,headers=header_request)

    # validaciones
    assert response.status_code == 204