from typing import List
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from requests import Session
from database.database import SessionLocal
from entities.employee.employee import Employee, EmployeeUpdate
from database.tables import *
import database.datasource as ds

employee_router = APIRouter(prefix="/employee", tags=["employees"])
        
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        
#Crud empleados
@employee_router.get(
    "/{id}", 
    status_code=status.HTTP_200_OK,
    # response_model=EmployeeModel
    )
def getEmployeeById(id: int, session: Session = Depends(get_session)):
    return ds.getEmployee(id, session)

@employee_router.get(
    "/employees/all",
    status_code=status.HTTP_200_OK,
    # response_model=List[Employee]
    )
def getEmployees(session: Session = Depends(get_session)):   
    try:
        return ds.getAllEmployees(session)
    except Exception as err:
        raise Exception(err)


@employee_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    )
def createEmployee(employee: Employee, session: Session = Depends(get_session)):
    return ds.createEmployee(employee, session)

@employee_router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    )
def updateEmployee(id: int, 
                   employee: EmployeeUpdate, 
                   session: Session = Depends(get_session)):
    return ds.updateEmployee(id, employee, session)

@employee_router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT
    )
def deleteEmployee(id: int, session: Session = Depends(get_session)):
    return ds.deleteEmployee(id, session)


