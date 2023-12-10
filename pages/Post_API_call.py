import requests

def post_api_call():
    post_url = "https://postman-integration-testing.glitch.me/"
    post_endpoint = "/register"

    main_url = post_url + post_endpoint
    headers = {}
    data = ""

    response = requests.request("POST", url=main_url, headers=headers, data=data)

    print(response)

    post_response = response.json()
    print(post_response)

    assert response.status_code == 200, (f"Expected Status code is 200, Actual status code is"
                                         f" {response.status_code}")

    assert "application/json" in response.headers.get("Content-Type"), \
        "Unexpected Content-Type in response headers"

    token_response = response.json()
    token_id = token_response.get('token')

    return response, token_id,token_response


response, token_id,token_response= post_api_call()
# print("Response:", response)
# print("Token ID:", token_id)
