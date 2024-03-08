from app.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class Vehicle(Base):
    __tablename__ = "vehicle"

    id = Column(Integer, primary_key=True)
    description = Column(String(255), nullable=False)
    plate = Column(String(20), nullable=False)
    brand = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    employee_id = Column(Integer, ForeignKey("employee.id"), nullable=False)

    employee = relationship('Employee')

    def __init__(self, description, plate, brand, model, employee_id):
        self.description = description
        self.plate = plate
        self.brand = brand
        self.model = model
        self.employee_id = employee_id

    def to_dict(self):
        data = {
            "id": self.id,
            "description": self.description,
            "plate": self.plate, 
            "brand": self.brand,
            "model": self.model,
            "employee": self.employee.relationship_to_dict()
        }

        return data

    def relationship_to_dict(self):
        data = {
            "id": self.id,
            "description": self.description,
            "plate": self.plate, 
            "brand": self.brand,
            "model": self.model,
        }

        return data

    def __repr__(self):
        return f"<Vehicle id: {self.id} employee_id: {self.employee_id} description: {self.description} plate: {self.plate} brand: {self.brand} model: {self.model}>"