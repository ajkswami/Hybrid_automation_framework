import requests
import jsonpath
import json


def find_user_get():
    base_url = "https://reqres.in/"
    end_point = "api/users"

    url = base_url + end_point

    headers = {}

    response = requests.get(url=url, headers=headers)

    # converts json to dict

    resp_dict = json.loads(response.text)
    support_url = resp_dict['support']['url']
    print(support_url)

    # print(response.status_code)
    # print(response.json())

    print(resp_dict)

    print(resp_dict['data'])

    return response, resp_dict


response, resp_dict = find_user_get()
