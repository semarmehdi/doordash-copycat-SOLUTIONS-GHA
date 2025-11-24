# tests/test_root.py
import httpx

BASE_URL = "http://localhost:8080"


def test_root_welcome_message():
    response = httpx.get(f"{BASE_URL}/")
    assert response.status_code == 200

    data = response.json()
    # Adapt these assertions if your actual response differs
    assert isinstance(data, dict)
    assert any(k in data for k in ["message", "detail", "welcome"])
