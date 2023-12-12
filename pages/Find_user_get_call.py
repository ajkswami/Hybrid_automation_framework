import requests
import jsonpath


def find_user_get():
    base_url = "https://reqres.in/"
    end_point = "api/users"

    url = base_url + end_point

    headers = {}

    response = requests.get(url=url, headers=headers)

    print(response.status_code)
    print(response.json())
    return response


response = find_user_get()
