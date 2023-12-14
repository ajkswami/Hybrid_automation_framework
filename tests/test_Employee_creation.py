# test_Employee_creation.py

# test_Employee_creation.py

from pages.Get_employee_details import get_employee

def test_get_employee_detail():
    response = get_employee()

    assert response.status_code == 200, f"Expected is 200, Actual is {response.status_code}"

# This line is not necessary when running the test with pytest
# test_get_employee_detail()
