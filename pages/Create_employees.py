import requests
import json


def create_employee():
    base_url = "http://localhost:1000"
    end_point = "/create-user"

    # Replace with the actual parameter value you want to use

    complete_url = base_url + end_point

    print(complete_url)

    headers = {}

    json_payload = {

        "first_name": "Nitesh",
        "last_name": "Reddy",
        "gender": "1",
        "email": "nith@gmail.com",
        "company": "HCL Pvt LTD",
        "phone": "8123416711",
        "salary": 25000,
        "designation": "Associate",
        "location": "Hyderabad",
        "isActive": True,
        "isDelete": False,
        "isIncrement": True
    }

    response = requests.post(url=complete_url, headers=headers,
                             data=json.dumps(json_payload))

    json_response = response.json()

    text_response = response.text

    print(text_response)
    print(json_response)

    return response,text_response,json_response


response,text_response,json_response = create_employee()

