from app.services.employeeService import EmployeeService


class EmployeePort:
    def __init__(self) -> None:
        pass

    def list_all_employees(self):
        return EmployeeService().list_all_employees()
    
    def view_one_employee(self, id):
        return EmployeeService().view_one_employee(id)

    def create_one_employee(self, request):
        return EmployeeService().create_one_employee(request)