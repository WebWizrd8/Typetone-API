import sys
import os
import pytest
from fastapi.testclient import TestClient

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
print (SCRIPT_DIR)
sys.path.append(os.path.dirname(SCRIPT_DIR))

from app.main import create_app

app = create_app()
client = TestClient(app = app)

@pytest.mark.asyncio
async def test_create_new_code_for_url():
    # Test for creating new shortcode for url
    request = {"url": "https://www.testlink.com", "shortcode": "abc123"}
    response = client.post("/shorten", json = request)

    assert response.status_code == 201
    assert response.json()["shortcode"] == "abc123"

    # Test for assigning random shortcode for url
    request = {"url": "https://www.newtestlink.com"}
    response = client.post("/shorten", json = request)

    assert response.status_code == 201
    assert response.json()["shortcode"] is not None

    # Test for duplicated shortcode
    request = {"url": "https://www.freshtestlink.com", "shortcode": "abc123"}
    response = client.post("/shorten", json = request)
    assert response.status_code == 409

    # Test for invalid shortcode
    request = {"url": "https://www.othertestlink.com", "shortcode": "bc@123"}
    response = client.post("/shorten", json = request)
    assert response.status_code == 412

def test_get_url():
    pass

def test_get_code_stats():
    pass