from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from core.database.database import Base, engine
import application.controllers.employee_controller as emp
import application.controllers.authentication_controller as auth

Base.metadata.create_all(bind = engine)

def create_app() -> FastAPI:
    application = FastAPI()
    application.add_middleware(GZipMiddleware)
    application.include_router(emp.employee_router)
    application.include_router(auth.auth_router)
    return application

app = create_app()

