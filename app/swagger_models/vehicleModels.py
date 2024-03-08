from pydantic import BaseModel

class VehicleRequest(BaseModel):
    description: str
    plate: str
    brand: str
    model: str
    employee_id: int