from pydantic import BaseModel
from typing import Optional

class VehicleRequest(BaseModel):
    description: str
    plate: str
    brand: str
    model: str
    employee_id: int

class VehicleEditRequest(BaseModel):
    description: Optional[str] = None
    plate: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    employee_id: Optional[int] = None