from app.ports.vehiclePort import VehiclePort
from app.swagger_models.vehicleModels import VehicleRequest


class VehicleAdapter:
    def __init__(self) -> None:
        pass

    def list_all_vehicles(self):
        return VehiclePort().list_all_vehicles()

    def view_one_vehicle(self, id):
        return VehiclePort().view_one_vehicle(id)

    def create_one_vehicle(self, request: VehicleRequest):
        data = request.model_dump()
        return VehiclePort().create_one_vehicle(data)

    def edit_one_vehicle(self, id, request: VehicleRequest):
        data = request.model_dump()
        return VehiclePort().edit_one_vehicle(id, data)

    def delete_one_vehicle(self, id):
        return VehiclePort().delete_one_vehicle(id)