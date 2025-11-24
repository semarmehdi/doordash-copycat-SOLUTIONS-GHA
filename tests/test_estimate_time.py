# tests/test_estimate_time.py
import httpx

BASE_URL = "http://localhost:8080"


def test_estimate_time_valid_distance():
    distance_km = 5
    response = httpx.get(f"{BASE_URL}/estimate-time/{distance_km}")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    # Example expected key, adapt to actual implementation
    assert "estimated_time_minutes" in data
    assert isinstance(data["estimated_time_minutes"], (int, float))
    assert data["estimated_time_minutes"] > 0


def test_estimate_time_invalid_distance():
    # Negative distance should normally be rejected
    distance_km = -3
    response = httpx.get(f"{BASE_URL}/estimate-time/{distance_km}")

    # Depending on how validation is implemented, you might get 400 or 422
    assert response.status_code in (400, 422)
