from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from database.database import Base, engine
import core.employee_controller as emp
import core.authentication_controller as auth

from entities.employee import Employee, EmployeeUpdate

Base.metadata.create_all(bind = engine)

def create_app() -> FastAPI:
    application = FastAPI()
    application.add_middleware(GZipMiddleware)
    application.include_router(emp.employee_router)
    # application.include_router(auth.auth_router)
    return application

app = create_app()

