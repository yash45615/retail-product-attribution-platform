from fastapi.testclient import (
    TestClient
)

from app.main import app


client = TestClient(app)


def test_attribution():

    response = client.post(
        "/api/attribute",
        json={
            "product_id": "TEST001",
            "title":
                "Nike Men's Running Shoes Black",
            "description":
                "Performance running shoes"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data[
        "product_id"
    ] == "TEST001"

    assert "product_type" in data

    assert "attributes" in data

    assert "confidence" in data