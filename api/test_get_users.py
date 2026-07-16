from utils.api_client import APIClient

client = APIClient()


def test_get_users():

    response = client.get("/users")

    print("Status Code :", response.status_code)

    data = response.json()

    assert response.status_code == 200

    assert len(data) == 10

    assert data[0]["name"] == "Leanne Graham"

    print("GET API Test PASSED")