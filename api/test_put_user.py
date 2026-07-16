import requests


def test_update_user():

    url = "https://reqres.in/api/users/2"

    payload = {"name": "Hamsika", "job": "Champion"}

    response = requests.put(url, json=payload)

    print(response.json())

    assert response.status_code == 200
