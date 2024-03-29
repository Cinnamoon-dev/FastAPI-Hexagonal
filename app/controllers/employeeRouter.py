from fastapi import APIRouter
from app.adapters.employeeAdapter import EmployeeAdapter
from app.swagger_models.employeeModels import EmployeeEditRequest, EmployeeRequest

router = APIRouter(prefix="/employee")

@router.get("/all")
def get_all_employee():
    return EmployeeAdapter().list_all_employees()

@router.get("/view/{id:int}")
def get_one_employee(id: int):
    return EmployeeAdapter().view_one_employee(id)

@router.post("/add")
def create_one_employee(employee: EmployeeRequest):
    return EmployeeAdapter().create_one_employee(employee)

@router.put("/edit/{id:int}")
def edit_one_employee(id: int, fields: EmployeeEditRequest):
    return EmployeeAdapter().edit_one_employee(id, fields)

@router.delete("/delete/{id:int}")
def delete_one_employee(id: int):
    return EmployeeAdapter().delete_one_employee(id)