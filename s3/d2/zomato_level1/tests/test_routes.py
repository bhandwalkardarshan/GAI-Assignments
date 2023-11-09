from app import app
import pytest

@pytest.fixture
def client():
    client = app.test_client()
    yield client

def test_hello_zesty_zomato(client):
    response = client.get('/')
    assert response.data == b'Hello, Zesty Zomato!'
