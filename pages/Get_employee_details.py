import requests


def get_employee():
    base_url = "http://localhost:1000"
    end_point = "/get-user/12"

    # Replace with the actual parameter value you want to use

    complete_url = base_url + end_point

    print(complete_url)

    headers = {}
    data = {}

    response = requests.get(url=complete_url, headers=headers, data=data)

    print(response.text)

    return response


response = get_employee()
