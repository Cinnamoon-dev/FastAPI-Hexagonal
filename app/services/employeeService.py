import json
from fastapi import Response
from app.database import get_db
from app.models.EmployeeModel import Employee
from app.services import instance_update

class EmployeeService:
    def __init__(self):
        pass

    def list_all_employees(self):
        db = get_db()
        employees = db.query(Employee).all()

        return {"data": [employee.relationship_to_dict() for employee in employees]}

    def view_one_employee(self, id):
        db = get_db()
        employee = db.query(Employee).get(id)

        if not employee:
            return Response(json.dumps({"error": True, "message": "Employee not found"}), 404) 

        return employee.to_dict()
    
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
 
    def edit_one_employee(self, id, request):
        db = get_db()
        employee = db.query(Employee).get(id)

        if not employee:
            return Response(json.dumps({"error": True, "message": "Employee not found"}), 404)

        instance_update(employee, request)

        try:
            db.commit()
            return Response(json.dumps({"error": False, "message": "Employee edited successfully"}))
        except:
            db.rollback()
            return Response(json.dumps({"error": True, "message": "Database Error"}, 500))

    def delete_one_employee(self, id):
        db = get_db()
        employee = db.query(Employee).get(id)

        if not employee:
            return Response(json.dumps({"error": True, "message": "Employee not found"}), 404)
        
        try:
            db.delete(employee)
            db.flush()
            db.commit()
            return Response(json.dumps({"error": False, "message": "Employee deleted successfully"}))
            
        except:
            db.rollback()
            return Response(json.dumps({"error": True, "message": "Database error"}), 500)