
import requests
import pytest




def test_find_user():

    response = find_user_get()

    #print(response)

    #print(response.status_code)
    assert response.status_code == 200 , (f"Expected is 200,"
                                          f"Actual is {response.status_code}")

    assert


test_find_user()




