from fastapi import APIRouter
from app.services.employeeService import EmployeeService
from app.swagger_models.employeeModels import EmployeeRequest

router = APIRouter(prefix="/employee")

# TODO
# Create Ports and Adapters

@router.get("/all")
def get_all_employee():
    return EmployeeService().list_all_employees()

@router.post("/add")
def create_one_employee(employee: EmployeeRequest):
    data = employee.model_dump()
    data["email"] = data["email"].lower()
    return EmployeeService().create_one_employee(data)