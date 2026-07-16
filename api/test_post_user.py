import requests


def test_create_user():

    url = "https://reqres.in/api/users"

    payload = {"name": "Hamsika", "job": "Student"}

    response = requests.post(url, json=payload)

    print(response.json())

    assert response.status_code == 201
