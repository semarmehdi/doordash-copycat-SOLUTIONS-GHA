# tests/test_calculate_fee.py
import httpx

BASE_URL = "http://localhost:8080"


def test_calculate_fee_valid_payload():
    payload = {
        "distance_km": 10.5,
        "weight_kg": 2.0,
    }
    response = httpx.post(f"{BASE_URL}/calculate-fee/", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert "delivery_fee" in data
    assert isinstance(data["delivery_fee"], (int, float))
    assert data["delivery_fee"] >= 0


def test_calculate_fee_invalid_payload():
    # Missing fields / invalid values
    payload = {
        "distance_km": -2,
        "weight_kg": -1,
    }
    response = httpx.post(f"{BASE_URL}/calculate-fee/", json=payload)
    # Again, 400 vs 422 depends on how FastAPI validation is wired
    assert response.status_code in (400, 422)
