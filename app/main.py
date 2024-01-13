from fastapi import FastAPI
from app.routers import router
from app.database.database import typetonedb

def create_app() -> FastAPI:
    _app = FastAPI()
    _app.include_router(router)

    return _app

app = create_app()

@app.on_event("startup")
async def startup():
    await typetonedb.connect()

@app.on_event("shutdown")
async def shutdown():
    await typetonedb.disconnect()