from typing import Optional

from pydantic import BaseModel, EmailStr


class ContactInfo(BaseModel):
    employee_id: int
    email: EmailStr
    phone: Optional[str]
    address: str
    