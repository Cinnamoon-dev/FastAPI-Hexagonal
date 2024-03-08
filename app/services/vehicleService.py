import json
from fastapi import Response
from app.database import get_db
from app.models.VehicleModel import Vehicle

class VehicleService:
    def __init__(self):
        pass

    def list_all_vehicles(self):
        db = get_db()
        data = db.query(Vehicle).all()

        return {"data": data}

    def view_one_vehicle(self, id):
        db = get_db()
        data = db.query(Vehicle).get(id)

        if not data:
            return Response(json.dumps({"error": True, "message": "Vehicle not found"}), 404) 

        return data 
    
    def create_one_vehicle(self, request):
        db = get_db()

        if db.query(Vehicle).filter(Vehicle.plate == request.get("plate")).first():
            return Response(json.dumps({"error": True, "message": "Plate already exists"}), 409)
        
        newVehicle = Vehicle(**request)
        db.add(newVehicle)

        try:
            db.flush()
            db.commit()
            return Response(json.dumps({"error": False, "message": "Vehicle created successfully"}), 200)
        except:
            db.rollback()
            return Response(json.dumps({"error": True, "message": "Database error"}), 500)