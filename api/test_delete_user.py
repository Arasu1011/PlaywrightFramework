import requests
from config.config import REQRES_API_KEY


def test_delete_user():

    url = "https://reqres.in/api/users/2"

    headers = {"x-api-key": REQRES_API_KEY}

    response = requests.delete(url, headers=headers)

    print("Status Code :", response.status_code)

    assert response.status_code == 204

    print("DELETE API Test PASSED")
