import uvicorn
from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter(prefix="")

@router.get("/test")
async def test():
    return {"test": "test"}

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)