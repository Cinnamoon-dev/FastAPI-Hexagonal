from pydantic import BaseModel
from typing import Optional

class EmployeeRequest(BaseModel):
    name: str
    email: str
    password: str
    wage: float

class EmployeeEditRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    wage: Optional[float] = None