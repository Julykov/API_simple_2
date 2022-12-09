import requests
import json
import jsonpath


def test_update_data():
    url = "https://reqres.in/api/users/2"

    file = open('input/UpdateUser.json', 'r')
    json_input = file.read()    # but this content is simply a string format
    request_json = json.loads(json_input)   # parse this file in a format of json

    response = requests.put(url, request_json)
    print(response.content)
    print()

    assert response.status_code == 200

    print(response.text)
    response_json = json.loads(response.text)
    updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
    print(updated_li[0])