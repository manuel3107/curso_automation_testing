import pytest

@pytest.fixture
def url_base():
        return 'https://reqres.in/api/users'
    
@pytest.fixture
def header_request():
        return {"x-api-key": "reqres-free-v1"}