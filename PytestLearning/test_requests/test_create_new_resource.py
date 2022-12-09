import requests
import json
import jsonpath
import pytest


@pytest.mark.Smoke
def test_new_resource():
    url = "https://reqres.in/api/users"

    file = open('input/CreateUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    print()

    response = requests.post(url, request_json)

    assert response.status_code == 201

    print(response.text)
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])
