from enum import Enum

from pydantic import BaseModel


class Department(BaseModel, Enum):
    # id: str
    name: str
    location: str