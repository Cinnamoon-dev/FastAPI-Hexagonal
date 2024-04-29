from app.database import Base
from sqlalchemy.orm import relationship
from app.models.VehicleModel import Vehicle
from sqlalchemy import Column, Integer, String, Float


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String, nullable=False)
    wage = Column(Float, nullable=False)
    
    vehicles = relationship(Vehicle, back_populates='employee')

    def __init__(self, name, email, password, wage):
        self.name = name
        self.email = email
        self.password = password
        self.wage = wage

    def to_dict(self):
        data = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "wage": self.wage,
            "vehicles": []
        }

        for i in self.vehicles:
            data["vehicles"].append(i.relationship_to_dict())

        return data

    def relationship_to_dict(self):
        data = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "wage": self.wage,
        }

        return data

    def __repr__(self):
        return f"<Employee id: {self.id} name: {self.name} email: {self.email} wage: {self.wage}>"