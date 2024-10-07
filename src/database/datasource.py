from typing import List
from fastapi import Depends, HTTPException
from entities.employee.employee import Employee, EmployeeUpdate
from database.tables import *
from database.database import Base, engine, SessionLocal
from sqlalchemy.orm import Session


def getEmployee(
    id: int,
    session: Session) -> EmployeeModel:
    employee = session.query(EmployeeModel).get(id) 

    if not employee:
        raise HTTPException(status_code=404, detail=f"Employee with id {id} not found")
    return employee

def getAllEmployees(session: Session) -> List[EmployeeModel]: 
    task_list = session.query(EmployeeModel).all() 
    return task_list

def createEmployee(
    employee: Employee,
    session: Session) -> dict[str, any]:
    employee_data = employee.model_dump()
    
    contact_info_data = employee_data.pop('contact_info')
    soft_skills_data = employee_data.pop('soft_skills', [])
    hard_skills_data = employee_data.pop('hard_skills', [])
    employee_db = EmployeeModel(**employee_data)
    # contact_db = ContactInfoModel(**contact_info_data)
    # def map_skills(skill_data, Model):
    #     return [Model(**skill) for skill in skill_data]
    
    # employee_db.soft_skills = map_skills(soft_skills_data, EmployeeSoftSkillsModel)
    # employee_db.hard_skills = map_skills(hard_skills_data, EmployeeHardSkillsModel)

    session.add(employee_db)
    session.commit()
    session.refresh(employee_db)

    return employee_data


def updateEmployee(
    id: int, 
    employee: EmployeeUpdate, 
    session: Session) -> dict[str, any]:
    employee_db = session.query(EmployeeModel).get(id)  # Get given id

    if employee_db:
        employee_data = employee.model_dump()

        # contact_info_data = employee_data.pop('contact_info')
        soft_skills_data = employee_data.pop('soft_skills')
        hard_skills_data = employee_data.pop('hard_skills')

        employee_db = EmployeeModel(**employee_data)
        # soft_skills_db = EmployeeSoftSkillsModel(**soft_skills_data)
        # hard_skills_db = EmployeeHardSkillsModel(**hard_skills_data)
        
        for key, value in employee_data.items():
            setattr(employee_db, key, value)
        # contact_info_db = ContactInfoModel(**contact_info_data)
        # employee_db.contact_info = contact_info_db
        # employee_db.soft_skills = soft_skills_db
        # employee_db.hard_skills = hard_skills_db

        employee_db = employee_data
        session.commit()
        session.refresh(employee_db)

    if not employee_db:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")

    return employee_db

def deleteEmployee(id: int, session: Session):
    employee_db = session.query(EmployeeModel).get(id)
    if employee_db:
        session.delete(employee_db)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")
    return None

