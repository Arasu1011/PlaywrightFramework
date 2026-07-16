from utils.api_client import APIClient

client = APIClient()


def test_create_user():

    payload = {
        "name": "Hamsika",
        "job": "Student"
    }

    response = client.post("/users", payload)

    print("Status Code :", response.status_code)
    print(response.json())

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Hamsika"
    assert data["job"] == "Student"

    print("POST API Test PASSED")