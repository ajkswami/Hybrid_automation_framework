import re
from pages.Post_API_call import post_api_call

def test_my_post_call():
    response, token_id ,token_response= post_api_call()

    assert response.status_code == 200, f"Expected Status code is 200, Actual status code is {response.status_code}"

    assert "application/json" in response.headers.get("Content-Type"), \
        "Unexpected Content-Type in response headers"

    assert re.match(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$', token_id), \
        f"Assertion failed: Expected a valid UUID format for token_id, but got {token_id}"



# Add the following line to call the test function
test_my_post_call()





