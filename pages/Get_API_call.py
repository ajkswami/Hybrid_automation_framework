


import requests

from pages.Post_API_call import response
from pages.Post_API_call import post_api_call,token_id,token_response




def get_call_api():
    get_url = "https://postman-integration-testing.glitch.me"
    get_endpoint = "/my-name"
    get_params = {"token": {token_id}}

    main_url = get_url + get_endpoint

    #print(main_url)

    payload = ""
    headers = {}

    #Actual reponse

    response = requests.request("GET", url=main_url, headers=headers, params=get_params, data=payload)



    # extract response

    token_response = response.json()

    #get name
    token_name = token_response.get('name')

    #match name

    if token_name is not None:
        print("Token Name:", token_name)
    else:
        print("The 'name' key is not present in the JSON response.")

    # extract keys

    token_keys = list(token_response.keys())
    if token_keys:
        print("First key in the JSON response:", token_keys[0])
    else:
        print("The JSON response is empty.")





    #print(response.text)

    # Assertions
    # Status code to be 403 for an invalid token
    assert response.status_code == 200 , f"Expected status code 403, Actual status code is {response.status_code}"
    #assert response.status_code == 403, f"Expected status code 403, Actual status code is {response.status_code}"

    return response,token_response,token_name,token_keys,token_id  # You can return the response object if needed

response,token_response,token_name,token_keys,token_id=get_call_api()
# You can continue with additional assertions or other processing based on the response.
