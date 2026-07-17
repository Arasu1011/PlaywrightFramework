import requests
from config.config import REQRES_API_KEY


def test_update_user():

    url = "https://reqres.in/api/users/2"

    payload = {"name": "Hamsika", "job": "Automation Engineer"}

    headers = {"x-api-key": REQRES_API_KEY}

    response = requests.put(url, json=payload, headers=headers)

    print("Status Code :", response.status_code)
    print(response.json())

    assert response.status_code == 200

    print("PUT API Test PASSED")
