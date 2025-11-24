import requests
import pytest

@pytest.mark.api
def test_delete_user(url_base,header_request):
    url = f"{url_base}/2"

    response = requests.delete(url, headers=header_request)

    assert response.status_code == 204
    assert response.text == ''