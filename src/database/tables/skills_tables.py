from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

class SoftSkillsModel(Base):
    __tablename__ = 'soft_skills'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(60), nullable=False)
    weight = Column(Integer, nullable=False)
    
class HardSkillsModel(Base):
    __tablename__ = 'hard_skills'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(60), nullable=False)
    weight = Column(Integer, nullable=False)
    