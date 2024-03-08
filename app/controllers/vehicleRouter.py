from fastapi import APIRouter
from app.services.vehicleService import VehicleService
from app.swagger_models.vehicleModels import VehicleRequest

router = APIRouter(prefix="/vehicle")

@router.get("/all")
def get_all_vehicles():
    return VehicleService().list_all_vehicles()

@router.get("/view/{id:int}")
def get_one_vehicle(id: int):
    return VehicleService().view_one_vehicle(id)

@router.post("/add")
def create_one_vehicle(vehicle: VehicleRequest):
    data = vehicle.model_dump()
    return VehicleService().create_one_vehicle(data)