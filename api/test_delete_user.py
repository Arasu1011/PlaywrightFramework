from utils.api_client import APIClient

client = APIClient()


def test_delete_user():

    response = client.delete("/users/1")

    print("Status Code :", response.status_code)

    assert response.status_code == 200

    print("DELETE API Test PASSED")