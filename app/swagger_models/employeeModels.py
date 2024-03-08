from pydantic import BaseModel

class EmployeeRequest(BaseModel):
    name: str
    email: str
    password: str
    wage: float