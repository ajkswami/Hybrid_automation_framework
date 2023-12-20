from pages.Create_employees import create_employee

response, text_response, json_response = create_employee()


def test_response_code():
    user_id = json_response['user']['user_id']

    print(user_id)

    assert response.status_code == 200 , (f"Expected : 200,"
                                          f"Actual : {response.status_code}")

    # assert json_response["message"] == "User created successfully"


def test_msg():
    assert json_response["message"] == "User created successfully"
    json_msg = json_response["message"]
    f"Expected : User created successfully ,Actual : json_msg  "



def test_dict_user():
    assert isinstance(json_response["user"], dict), \
        (f"Expected 'user_id' to be an Dict, but got"
         f" {type(json_response['user'])}")




def test_user_id():
    assert isinstance(json_response["user"]["user_id"], int)
