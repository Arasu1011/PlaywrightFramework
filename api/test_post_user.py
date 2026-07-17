import requests
from config.config import REQRES_API_KEY


def test_create_user():

    url = "https://reqres.in/api/users"

    payload = {"name": "Hamsika", "job": "Student"}

    headers = {"x-api-key": REQRES_API_KEY}

    response = requests.post(url, json=payload, headers=headers)

    print("Status Code :", response.status_code)
    print(response.json())

    assert response.status_code == 201

    print("POST API Test PASSED")
