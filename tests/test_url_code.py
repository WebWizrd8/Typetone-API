import sys
import os
import pytest
from fastapi.testclient import TestClient

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
print (SCRIPT_DIR)
sys.path.append(os.path.dirname(SCRIPT_DIR))

from app.main import create_app
from app.utils.shortcode import create_random_code

app = create_app()
client = TestClient(app = app)

code = create_random_code(6)
link = "https://www.testlink.com"

@pytest.mark.asyncio
async def test_create_new_code_for_url():
    # Test for creating new shortcode for url
    request = {"url": "https://www.testlink.com", "shortcode": code}
    response = client.post("/shorten", json = request)

    assert response.status_code == 201
    assert response.json()["shortcode"] == code

    # Test for assigning random shortcode for url
    request = {"url": "https://www.testlink.com"}
    response = client.post("/shorten", json = request)

    assert response.status_code == 201
    assert response.json()["shortcode"] is not None

    # Test for duplicated shortcode
    request = {"url": "https://www.testlink.com", "shortcode": code}
    response = client.post("/shorten", json = request)
    assert response.status_code == 409

    # Test for invalid shortcode
    request = {"url": "https://www.testlink.com", "shortcode": "bc@123"}
    response = client.post("/shorten", json = request)
    assert response.status_code == 412

def test_get_url():
    result = client.get("/" + code)
    assert result.status_code == 302
    assert result.json()["url"] == link

    result = client.get("/" + create_random_code(6))
    assert result.status_code == 404

def test_get_code_stats():
    result = client.get("/" + code + "/stats")
    assert result.status_code == 200

    result = client.get("/" + create_random_code(6))
    assert result.status_code == 404