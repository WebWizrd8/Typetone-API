from fastapi.testclient import TestClient
from ..app.main import create_app

app = create_app()
client = TestClient(app = app)

def test_create_new_code_for_url():
    request = {"url": "https://www.testlink.com", "shortcode": "abc123"}
    response = client.post("/shorten", json = request)

    assert response.status_code == 201
    assert response.json()["shortcode"] == "abc123"

def test_create_random_code_for_url():
    request = {"url": "https://www.testlink.com"}
    response = client.post("/shorten", json = request)

    assert response.status_code == 201
    assert response.json()["shortcode"] is not None

def test_duplicated_code():
    request = {"url": "https://www.testlink.com", "shortcode": "abc123"}
    response = client.post("/shorten", json = request)

    assert response.status_code == 409

def test_invalid_code():
    request = {"url": "https://www.testlink.com", "shortcode": "Q@3dh4"}
    response = client.post("/shorten", json = request)

    assert response.status_code == 412

def test_get_url():
    pass

def test_get_code_stats():
    pass