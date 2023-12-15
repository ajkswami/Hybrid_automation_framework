# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

'''''

import requests

# Authentication URL
auth_url = "https://reqres.in/api/login"

resource_url = "https://reqres.in/api/protected/resource"

#
credentials = {"email": "eve.holt@reqres.in", "password": "cityslicka"}

# Step 1: Authentication to obtain a token
auth_response = requests.post(auth_url, json=credentials)

# Check if authentication was successful
if auth_response.status_code == 200:
    # Extract the token from the authentication response
    token = auth_response.json().get('token')
    print(f"Authentication successful. Token: {token}")

    # Step 2: Use the obtained token for subsequent requests
    headers = {"Authorization": f"Bearer {token}"}
    resource_response = requests.get(resource_url, headers=headers)

    # Check if the request to the protected resource was successful
    if resource_response.status_code == 200:
        print("Access to the protected resource granted.")
    else:
        print(f"Access to the protected resource failed. Status code: {resource_response.status_code}")
else:
    print(f"Authentication failed. Status code: {auth_response.status_code}, Response: {auth_response.text}")
'''''