from utils.api_client import APIClient

client = APIClient()


def test_update_user():

    payload = {
        "name": "Hamsika",
        "job": "Automation Engineer"
    }

    response = client.put("/users/1", payload)

    print(response.json())

    assert response.status_code == 200

    data = response.json()

    assert data["job"] == "Automation Engineer"

    print("PUT API Test PASSED")