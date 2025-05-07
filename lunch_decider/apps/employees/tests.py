import pytest

# Create your tests here.
@pytest.mark.django_db
def test_employee_serializer():
    employee = Employee.objects.create(first_name="John", last_name="Doe", email="john@example.com")
    serializer = EmployeeSerializer(employee)
    assert serializer.data["first_name"] == "John"
    assert serializer.data["email"] == "john@example.com"