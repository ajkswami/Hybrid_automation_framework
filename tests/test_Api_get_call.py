# test_file.py
import re
from pages.Get_API_call import get_call_api


def test_my_api_call():
    response, token_response, token_name, token_keys, token_id = get_call_api()

    assert response.status_code == 200, f"Expected status code 403, Actual status code is {response.status_code}"

    assert token_name, "Token name should not be empty"

    assert re.match(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$', token_id), \
        f"Assertion failed: Expected a valid UUID format for token_id, but got {token_id}"


test_my_api_call()
