from pydantic import BaseModel


class Ability(BaseModel):
    name: str
    domain: int
    weight: int