import uvicorn
from fastapi import FastAPI
from app.database import Base, engine
from app.controllers import employeeRouter, vehicleRouter

app = FastAPI()

app.include_router(employeeRouter.router)
app.include_router(vehicleRouter.router)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    uvicorn.run('main:app', host='0.0.0.0')