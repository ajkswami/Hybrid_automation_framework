

import sys
import os

from pages.Get_employee_details import get_employee, response
import requests

import sys
sys.path.append(r"C:\Users\pc\Desktop\MyProjects\API_Automation"
                r"\My_API_project\Hybrid_automation_framework")

from pages.Get_employee_details import get_employee

import json

import pytest
import jsonpath




def test_detail():
    response = get_employee()


     # Assertion for Status Code
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    return response  # Return the entire response

'''''
def test_length():
    response = test_get_user_detail()

    # Assertion for Length (Assuming the response is a single user)
    assert len(response["user"]) > 0, "User data is empty"
    return response

def test_user_isActive():
    response = test_get_user_detail()

    # Additional Assertions based on your requirements
    assert response["user"]["isActive"], "User is not active"

    # If you need to compare the value, you can store it in a variable
    test_value = response["user"]["isActive"]

    # Perform additional comparisons if needed
    assert test_value, "User is not active"

    # Assertion for Status Code


'''






