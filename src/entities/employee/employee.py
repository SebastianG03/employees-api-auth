from typing import Optional
from pydantic import BaseModel

from .contact_info import ContactInfo
from .hard_skills import HardSkills
from .soft_skills import SoftSkills


class Employee(BaseModel):
    name: str
    password: str
    contact_info: ContactInfo
    department_id: int
    position_id: int
    salary: float
    soft_skills: Optional[list[SoftSkills]] = []
    hard_skills: Optional[list[HardSkills]] = []  
    
    class Config:
        orm_mode = True
        from_attributes=True

        
    
    
class EmployeeUpdate(BaseModel):
    id: int
    name: str
    password: str
    contact_info: ContactInfo
    department_id: int
    position_id: int
    salary: float
    soft_skills: list[SoftSkills] = []
    hard_skills: list[HardSkills] = []
    
    class Config:
        orm_mode = True
        from_attributes=True