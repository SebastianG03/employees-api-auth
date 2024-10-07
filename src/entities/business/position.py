from enum import Enum

from pydantic import BaseModel


class Position(BaseModel, Enum):
    # id: int
    name: str