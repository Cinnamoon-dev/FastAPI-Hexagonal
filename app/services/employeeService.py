import json
from fastapi import Response
from app.database import get_db
from app.models.EmployeeModel import Employee

class EmployeeService:
    def __init__(self):
        pass

    def list_all_employees(self):
        db = get_db()
        data = db.query(Employee).all()

        return {"data": data}

    def view_one_employee(self, id):
        db = get_db()
        data = db.query(Employee).get(id)

        return {"data": data}
    
    def create_one_employee(self, request):
        db = get_db()
        email = request.get("email").lower()

        if db.query(Employee).filter(Employee.email == email).first():
            return Response(json.dumps({"error": True, "message": "email already exists"}), 409)
        
        newEmployee = Employee(**request)
        db.add(newEmployee)

        try:
            db.flush()
            db.commit()
            return Response(json.dumps({"error": False, "message": "Employee created successfully"}), 200)
        except:
            db.rollback()
            return Response(json.dumps({"error": True, "message": "Database error"}), 500)
 