# tests/tests_delete_token.py
from pages.Delete_API_call import Delete_Api
from pages.Post_API_call import post_api_call

def test_delete_api():
    response, token_id = Delete_Api()


    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    # Add more assertions as needed


    assert isinstance(token_id, str), f"Expected token_id to be a string, but got {type(token_id)}"
    # Add more assertions related to token_id as needed
test_delete_api()