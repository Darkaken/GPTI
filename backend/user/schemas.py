from pydantic import EmailStr

from datetime import date
from typing import Optional

from user.schemas_validation import BaseSchemaUser

class UserCreate(BaseSchemaUser, validate_assignment=True):

    name: str
    email: EmailStr
    password: Optional[str] = None


class UserUpdate(BaseSchemaUser, validate_assignment=True):

    id: str
    name: Optional[str] = None

class UserOut(BaseSchemaUser):

    id: str
    name: str
    email: EmailStr

    class Config:

        validate_assignment = True
        orm_mode = True