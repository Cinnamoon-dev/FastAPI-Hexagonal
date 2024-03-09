from app.services.vehicleService import VehicleService
from app.swagger_models.vehicleModels import VehicleRequest


class VehiclePort:
    def __init__(self) -> None:
        pass

    def list_all_vehicles(self):
        return VehicleService().list_all_vehicles()

    def view_one_vehicle(self, id):
        return VehicleService().view_one_vehicle(id)

    def create_one_vehicle(self, request: VehicleRequest):
        return VehicleService().create_one_vehicle(request)

    def delete_one_vehicle(self, id):
        return VehicleService().delete_one_vehicle(id)