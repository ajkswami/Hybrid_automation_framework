import requests


def get_employee():
    base_url = "http://localhost:1000"
    end_point = "/get-user/24"

    complete_url = base_url + end_point

    headers = {}
    data = {}

    response = requests.get(url=complete_url, headers=headers, data=data)

    # Ensure the response is successful (status code 200)
    assert response.status_code == 200, f"Request failed with status code {response.status_code}"

    # Convert response content to JSON
    #response_json = response.text

    #print(response_json)

    # Assertion for Length (Assuming the response is a single user)
    #assert len(response_json["user"]) > 0, "User data is empty"

    return response,complete_url


response,complete_url = get_employee()
