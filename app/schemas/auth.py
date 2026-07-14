from typing import Self
import re
from uuid import UUID
from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    model_validator,
)

from app.enums.user_role import UserRole


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


class VerifyOTPRequest(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True
    )
    email: EmailStr
    otp: str = Field(
        min_length=6,
        max_length=6,
        pattern=r"^\d{6}$",
        description="A 6-digit OTP code."
    )


class VerifyOTPResponse(BaseModel):
    message: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse

class UserResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID
    username: str
    email: EmailStr
    first_name: str | None
    last_name: str | None
    role: UserRole
    is_verified: bool