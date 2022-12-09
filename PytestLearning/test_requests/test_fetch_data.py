import requests
import json
import jsonpath


def test_fetch_data():
    url = "https://reqres.in/api/users?page=2"

    response = requests.get(url)
    print(response.text)

    json_response = json.loads(response.text)

    pages = jsonpath.jsonpath(json_response, 'total_pages')
    print()
    print(pages)
    print(pages[0])
    assert pages[0] == 2

    print(jsonpath.jsonpath(json_response, 'total'))
    print(jsonpath.jsonpath(json_response, 'support'))

    first_name = jsonpath.jsonpath(json_response, 'data[0].first_name')
    print(first_name)
    print(first_name[0])
    first_name_3 = jsonpath.jsonpath(json_response, 'data[2].first_name')
    print(first_name_3[0])


    print()
    print("=== Show 3 first names from data")
    for i in range(0,3):
        first_name_i = jsonpath.jsonpath(json_response, 'data['+ str(i) + '].first_name')
        print(first_name_i[0])