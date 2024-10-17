from fastapi import HTTPException
from sqlalchemy import Sequence
from sqlalchemy.orm import Session

from entities.tables.skills_tables import HardSkillsModel, SoftSkillsModel
from entities.tables.employee_skills_tables import EmployeeHardSkillsModel, EmployeeSoftSkillsModel
from entities.employee.hard_skills import HardSkills
from entities.employee.soft_skills import SoftSkills


### Hard skills table
def post_hard_skills(
    hard_skill: HardSkills, 
    session: Session) -> dict[str, any]:
    hard_skills_db = HardSkillsModel()
    hard_skills_db.name = hard_skill.name
    hard_skills_db.weight = hard_skill.weight
    
    session.add(hard_skills_db)
    session.commit()
    session.refresh(hard_skills_db)
    
    return hard_skill.model_dump()

def get_hard_skills(session: Session) -> HardSkillsModel:
    hard_skills = session.query(HardSkillsModel).all()
    return hard_skills

def update_hard_skills(id: int, skills: HardSkills, session: Session):
    skills_db = session.execute(HardSkillsModel).get(id)
    
    if skills_db:
        skills_db.id = id
        skills_db.name = skills.name
        skills_db.weight = skills.weight
        
        session.commit()
        session.refresh(skills_db)
    else:
        raise HTTPException(status_code=404, detail=f"Hard Skill with id {id} not found")
    return skills_db


### Soft Skils Table
def post_soft_skills(
    soft_skill: SoftSkills, 
    session: Session) -> dict[str, any]:
    soft_skills_db = SoftSkillsModel()
    soft_skills_db.name = soft_skill.name
    soft_skills_db.weight = soft_skill.weight
    
    session.add(soft_skills_db)
    session.commit()
    session.refresh(soft_skills_db)
    
    return soft_skill.model_dump()

def get_soft_skills(session: Session) -> SoftSkillsModel:
    soft_skills = session.query(SoftSkillsModel).all()
    return soft_skills

def update_soft_skills(id: int, skills: SoftSkills, session: Session):
    skills_db = session.execute(SoftSkillsModel).get(id)
    
    if skills_db:
        skills_db.id = id
        skills_db.name = skills.name
        skills_db.weight = skills.weight
        
        session.commit()
        session.refresh(skills_db)
    else:
        raise HTTPException(status_code=404, detail=f"Soft Skill with id {id} not found")
    return skills_db

### User Skills table

def get_user_soft_skills(
    employee_id: int, 
    session: Session) -> Sequence[EmployeeSoftSkillsModel]:
    statement = session.query(EmployeeSoftSkillsModel).where(
        EmployeeSoftSkillsModel.employee_id == employee_id)
    result = session.execute(statement)
    return result.scalars().all()

def get_user_hard_skills(
    employee_id: int, 
    session: Session) -> Sequence[EmployeeHardSkillsModel]:
    statement = session.query(EmployeeHardSkillsModel).where(
        EmployeeHardSkillsModel.employee_id == employee_id)
    result = session.execute(statement)
    return result.scalars().all()

### Post employee Skills 

def post_user_soft_skills(
    employee_id: int, 
    soft_skill_id: int,
    domain: int,
    session: Session
) -> dict[str, any]:
    soft_skill_db = EmployeeSoftSkillsModel()
    soft_skill_db.soft_skill_id = soft_skill_id
    soft_skill_db.employee_id = employee_id
    soft_skill_db.domain = domain
    
    session.add(soft_skill_db)
    session.commit()
    session.refresh(soft_skill_db)
    
    return {
        'employee_id:': employee_id,
        'soft_skill_id:': soft_skill_id,
        'domain:': domain 
    }
    
def update_user_soft_skills(
    employee_id: int,
    skills_id: int,
    domain: int,
    session: Session):
        statement = session.query(EmployeeSoftSkillsModel).where(
            EmployeeSoftSkillsModel.employee_id == employee_id and
            EmployeeSoftSkillsModel.soft_skill_id == skills_id )
        result = session.execute(statement)
        skills_db = result.scalars().first()

        if skills_db:
            skills_db.id = id
            skills_db.name = skills_id
            skills_db.domain = domain

            session.commit()
            session.refresh(skills_db)
        else:
            raise HTTPException(status_code=404, detail=f"Soft Skill with id {id} not found")
        return skills_db

def post_user_hard_skills(
    employee_id: int, 
    hard_skill_id: int,
    domain: int,
    session: Session
) -> dict[str, any]:
    hard_skill_db = EmployeeHardSkillsModel()
    hard_skill_db.hard_skill_id = hard_skill_id
    hard_skill_db.employee_id = employee_id
    hard_skill_db.domain = domain
    
    session.add(hard_skill_db)
    session.commit()
    session.refresh(hard_skill_db)
    
    return {
        'employee_id:': employee_id,
        'hard_skill_id:': hard_skill_id,
        'domain:': domain 
    }
    
def update_user_hard_skills(
    employee_id: int,
    skills_id: int,
    domain: int,
    session: Session):
        statement = session.query(EmployeeHardSkillsModel).where(
            EmployeeHardSkillsModel.employee_id == employee_id and
            EmployeeHardSkillsModel.hard_skill_id == skills_id )
        result = session.execute(statement)
        skills_db = result.scalars().first()

        if skills_db:
            skills_db.id = id
            skills_db.name = skills_id
            skills_db.domain = domain

            session.commit()
            session.refresh(skills_db)
        else:
            raise HTTPException(status_code=404, detail=f"Hard Skill with id {id} not found")
        return skills_db