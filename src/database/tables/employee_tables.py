from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

class EmployeeModel(Base):
    __tablename__ = 'employees'

    # Columnas básicas
    id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(String(265), nullable=False)
    name = Column(String(60), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)  # Asume que hay una tabla 'departments'
    position_id = Column(Integer, nullable=False)
    salary = Column(Float, nullable=False)
    soft_skills = relationship("SoftSkillsModel", secondary="employee_soft_skills")
    hard_skills = relationship("HardSkillsModel", secondary="employee_hard_skills")
    
    contact_info = relationship("ContactInfoModel", uselist=False, back_populates="employee")
     

class ContactInfoModel(Base):
    __tablename__ = 'contact_info'

    employee_id = Column(Integer, ForeignKey('employees.id'), primary_key=True)
    email = Column(String(120), nullable=False)
    phone = Column(String(20), nullable=False)
    address = Column(String(120), nullable=True)
    employee = relationship("EmployeeModel", back_populates="contact_info")
