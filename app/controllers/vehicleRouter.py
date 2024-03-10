from fastapi import APIRouter
from app.adapters.vehicleAdapter import VehicleAdapter
from app.swagger_models.vehicleModels import VehicleEditRequest, VehicleRequest

router = APIRouter(prefix="/vehicle")

@router.get("/all")
def get_all_vehicles():
    return VehicleAdapter().list_all_vehicles()

@router.get("/view/{id:int}")
def get_one_vehicle(id: int):
    return VehicleAdapter().view_one_vehicle(id)

@router.post("/add")
def create_one_vehicle(vehicle: VehicleRequest):
    return VehicleAdapter().create_one_vehicle(vehicle)

@router.put("/edit/{id:int}")
def edit_one_vehicle(id: int, fields: VehicleEditRequest):
    return VehicleAdapter().edit_one_vehicle(id, fields)

@router.delete("/delete/{id:int}")
def delete_one_vehicle(id: int):
    return VehicleAdapter().delete_one_vehicle(id)