import uvicorn
from app.database import Base, engine
from app.controllers import employeeRouter, vehicleRouter
from fastapi import FastAPI

app = FastAPI()

app.include_router(employeeRouter.router)
app.include_router(vehicleRouter.router)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    uvicorn.run('main:app', reload=True)