import pytest
from assertpy import assert_that
import json
import requests
from assertpy import assert_that
from cerberus import Validator



from pages.Get_employee_details import get_employee, complete_url

response,complete_url = get_employee()
resp_data = response.json()


def test_resp_status_code():
    assert response.status_code == 200, (f"Expected value : 200,"
                                         f"Actual value is {response.status_code}")


def test_content_type():
    content_typ = response.headers["Content-Type"]
    assert content_typ == "application/json; charset=utf-8" ,\
        f"Expected : application/json; charset=utf-8 ,Actual is {content_typ}"



def test_content_length():
    content_length = response.headers["Content-Length"]
    assert  content_length == "355"

def test_cookies():
    var = response.cookies

    assert not var

def test_length():
    resp_len = response.json()
    assert len(resp_len)==2 , f"Expected : 2 , Actual is {len(resp_len)}"


def test_resp_time():
    resp_time = response.elapsed.total_seconds()
    assert  resp_time < 0.5 ,f"Actual time is {resp_time} is less than Expected"


def test_message():
    user_found = resp_data['message']

    assert user_found == "User found" , f"Expected is User found ,Actual is {user_found}"

def test_user_dict():
    user_arr = resp_data['user']
    Actual_val = type(user_arr)
    assert  isinstance(user_arr,dict) , f"Expected is DICT, Actual is {Actual_val}"


def test_resp_val_user_id():

    assert resp_data["user"]["user_id"] == 24

def test_dtype_user_id():
    user_id = resp_data["user"]["user_id"]
    user_id_type = user_id
    assert  isinstance(user_id,int) , f"Expected is Integer,Actual is {user_id_type}"


def test_val_first_name():
    assert resp_data["user"]["first_name"]=="Manisha"


def test_dtype_first_name():
    first_name= resp_data["user"]["first_name"]
    first_name_type = type(first_name)

    assert  isinstance(first_name,str) , f"Expected dtype is (str),Actual is {first_name_type}"

def test_var_len_first_name():
    max_len = 7
    first_name_len = len(resp_data["user"]["first_name"])

    assert_that(first_name_len).is_equal_to(max_len)

def test_not_empty():
    assert resp_data is not None
    assert resp_data.get("user") is not None and resp_data.get("message") is not None



def test_isActive():
    assert resp_data["user"]["isActive"] == True


def test_isDeelete():
    Deelet = resp_data["user"]["isDelete"]
    assert  Deelet == False , f"Expected : False , Actual is {Deelet}"

def test_iscreated():
    user_created = resp_data["user"]["user_created_at"]
    user_updated = resp_data["user"]["user_updated_at"]

    assert  user_created and user_updated is not None , (f"Expected is data , Actual is "
                                                         f"{user_created}{user_updated}")

# Handling multiple userids through parametrization
test_data= [(24,"Manisha"),(25,"Mounika"),(26,"Somesh")]
@pytest.mark.parametrize("user_id,expected_name",test_data)
def test_check_multiple_responses_of_users(user_id,expected_name):
    response = requests.get(f"http://localhost:1000/get-user/{user_id}")
    response_data = response.json()
    assert response_data["user"]["first_name"] == expected_name



user_data = [(24,"manisha@yahoo.com"),(25,"mounika@gmail.com"),(26,"somesh@gmail.com")]

@pytest.mark.parametrize("user_id,expected_val",user_data)
def test_user_data(user_id,expected_val):
    r= requests.get(f"http://localhost:1000/get-user/{user_id}")
    r_data = r.json()
    assert r_data["user"]["email"] == expected_val





