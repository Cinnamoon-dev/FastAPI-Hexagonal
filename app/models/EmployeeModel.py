from app.database import Base
from sqlalchemy import String
from app.models.VehicleModel import Vehicle
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    wage: Mapped[float] = mapped_column(nullable=False)

    vehicles: Mapped[list[Vehicle]] = relationship(Vehicle, back_populates='employee')

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