
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "online"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_info_endpoint():
    response = client.get("/info")

    assert response.status_code == 200
    assert response.json()["version"] == "1.0.0"


def test_nonexistent_endpoint():
    response = client.get("/hello")

    assert response.status_code == 404
