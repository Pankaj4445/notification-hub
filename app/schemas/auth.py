from typing import Self
import re
from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    model_validator,
)

class RegisterRequest(BaseModel):

    model_config = ConfigDict(
        str_strip_whitespace=True
    )

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

    @model_validator(mode="after")
    def validate_passwords(self) -> Self:
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match.")

        return self

class RegisterResponse(BaseModel):

    message: str

    email: EmailStr