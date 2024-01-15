from fastapi import FastAPI
from app.routers import router

def create_app() -> FastAPI:
    _app = FastAPI()
    _app.include_router(router)

    return _app

app = create_app()