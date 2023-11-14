

from pydantic import BaseModel, field_validator, model_validator
from fastapi import Depends, HTTPException, status

from common.exceptions import *

class Base(BaseModel):

    @field_validator("name", check_fields=False)
    def check_name(cls, value: str) -> str:
        if not value.isalpha():
            raise InvalidNameError(message="Name not alphanumeric")
        if len(value) <= 2:
            raise InvalidNameError(message="Name too short")
        return value

class BaseSchemaUser(Base):

    @field_validator("password", check_fields=False)
    def check_password(cls, value: str) -> str:
        if len(value) <= 8:
            raise InvalidPasswordError(message="Password too short")
        return value

        # por lo menos una mayusc
        # por lo menos un numero