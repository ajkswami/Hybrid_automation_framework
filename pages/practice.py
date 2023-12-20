import json

import requests
from assertpy import assert_that
from cerberus import Validator

from Get_employee_details import get_employee

response = get_employee()


# def resp():
#     data = response.text
#     #print(data)
#     #print(response.headers)
#     user= resp_data["user"]["user_id"]
#     #print(user)
#
#
#
# resp()

def read_one_operation_has_expected_schema():
    schema = {
        "message": {'type': 'string', 'allowed': ['User found']},
        "user": {
            'type': 'dict',
            'schema': {
                "user_id": {'type': 'integer'},
                "first_name": {'type': 'string'},
                "last_name": {'type': 'string'},
                "gender": {'type': 'integer'},
                "email": {'type': 'string'},
                "company": {'type': 'string'},
                "phone": {'type': 'integer'},
                "salary": {'type': 'float'},
                "designation": {'type': 'string'},
                "location": {'type': 'string'},
                "isActive": {'type': 'integer'},
                "isDelete": {'type': 'integer'},
                "isIncrement": {'type': 'integer'},
                "user_created_at": {'type': 'datetime'},
                "user_updated_at": {'type': 'datetime'}
            }
        }
    }

    complete_url = "http://localhost:1000/get-user/24"  # Replace with the actual URL
    response = requests.get(complete_url)
    person = json.loads(response.text)

    validator = Validator(schema)
    is_valid = validator.validate(person)

    if not is_valid:
        print("Validation errors:", validator.errors)

    assert_that(is_valid).is_true()

read_one_operation_has_expected_schema()



