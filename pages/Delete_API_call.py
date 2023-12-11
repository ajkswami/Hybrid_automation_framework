import requests
import json

from pages.Post_API_call import  token_id


def Delete_Api():
    post_url = "https://postman-integration-testing.glitch.me/"
    post_endpoint = "/unregister"

    main_url = post_url + post_endpoint
    headers = {
        'Content-Type': 'application/json'
    }

    print(token_id)

    payload = json.dumps({"token": token_id})

    response = requests.request("POST", url=main_url, headers=headers, data=payload)

    print(response.text)

    assert response.status_code == 200, f"expected is 200 , actual is {response.status_code}"
    return response, token_id


response,token_id = Delete_Api()
