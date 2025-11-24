# tests/test_status.py
import httpx

BASE_URL = "http://localhost:8080"


def test_status_endpoint_ok():
    response = httpx.get(f"{BASE_URL}/status/")
    assert response.status_code == 200

    data = response.json()
    # Expected shape can be adapted to the real app
    assert isinstance(data, dict)
    # Typical choice for a simple status endpoint:
    assert "status" in data
    assert isinstance(data["status"], str)
