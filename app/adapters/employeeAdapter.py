from app.ports.employeePort import EmployeePort
from app.swagger_models.employeeModels import EmployeeEditRequest, EmployeeRequest


class EmployeeAdapter:
    def __init__(self) -> None:
        pass

    def list_all_employees(self):
        return EmployeePort().list_all_employees()
    
    def view_one_employee(self, id):
        return EmployeePort().view_one_employee(id)

    def create_one_employee(self, request: EmployeeRequest):
        data = request.model_dump()
        data['email'] = data['email'].lower()

        return EmployeePort().create_one_employee(data)

    def edit_one_employee(self, id, request: EmployeeEditRequest):
        data = request.model_dump()
        return EmployeePort().edit_one_employee(id, data)

    def delete_one_employee(self, id):
        return EmployeePort().delete_one_employee(id)