import requests
import pytest

import sys
sys.path.append(r"C:\Users\pc\Desktop\MyProjects\API_Automation"
                r"\My_API_project\Hybrid_automation_framework")


from pages.Find_user_get_call import find_user_get


def test_get_request_status_code():
    response, resp_dict = find_user_get()

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


test_get_request_status_code()



def test_find_user():
    response,resp_dict = find_user_get()

    # print(response)

    # print(response.status_code)
    data = response.json()

    #print(data)
    assert response.status_code == 200, (f"Expected is 200,"
                                         f"Actual is {response.status_code}")

    assert "page" in resp_dict, "Response contains page in data"


test_find_user()


def test_get_request_status_code():
    response,resp_dict = find_user_get()
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


test_get_request_status_code()



def test_json_response_content():
    response,resp_dict = find_user_get()
    resp_data = response.json()
    support_url = resp_dict['support']['url']
    print(support_url)


    assert "total_pages" in resp_data, "Key 'total_pages'  found in JSON response"
    assert support_url == "https://reqres.in/#support-heading", f"Expected be correct"

test_json_response_content()


