#import re
from pages.Get_API_call import get_call_api
#from pages.Delete_API_call import Delete_Api



def test_get_call():
    response, token_response, token_name, token_keys, token_id = get_call_api()

    assert response.status_code == 200, (f"Expected status code 403,"
                                         f" Actual status code is {response.status_code}")

    print(token_response)

    print(response)

    assert token_response is not None

    #assert token_name, "Token name should not be empty"


