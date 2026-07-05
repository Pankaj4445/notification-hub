from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    model_validator
)

from typing import Self
import re

class RegisterRequest(BaseModel):

    username: str = Field(
        min_length=3,
        max_length=30
    )

    email: EmailStr

    first_name: str = Field(
        min_length=2,
        max_length=50
    )

    last_name: str = Field(
        min_length=2,
        max_length=50
    )

    password: str

    confirm_password: str

class RegisterResponse(BaseModel):

    message: str

    email: EmailStr