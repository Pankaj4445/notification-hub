from fastapi import APIRouter, Depends

from app.api.dependencies import get_auth_service
from app.schemas.auth import (
 RegisterRequest,
 RegisterResponse, 
 VerifyOTPRequest, 
 VerifyOTPResponse, 
 LoginResponse, 
 LoginRequest, 
 UserResponse, 
 ForgotPasswordResponse, 
 ForgotPasswordRequest,
 ResetPasswordResponse,
 ResetPasswordRequest
 )
from app.services.auth_service import AuthService
from app.security.dependencies import get_current_user
from app.models import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=RegisterResponse,
)
async def register(
    request: RegisterRequest,
    service: AuthService = Depends(get_auth_service),
):
    return await service.register(request)

@router.post(
    "/verify-otp",
    response_model=VerifyOTPResponse,
)
async def verify_otp(
    request: VerifyOTPRequest,
    service: AuthService = Depends(get_auth_service),
):
    return await service.verify_otp(request)

@router.post(
    "/login",
    response_model = LoginResponse,
)
async def login(
    request: LoginRequest,
    service: AuthService = Depends(get_auth_service),
):
    return await service.login(request)

@router.get(
    "/me",
    response_model=UserResponse,
)
async def get_me(
    current_user: User = Depends(get_current_user),
) -> UserResponse:
    return UserResponse.model_validate(current_user)

@router.post("/forgot-password",
            response_model=ForgotPasswordResponse)
async def forgot_password(
    request:ForgotPasswordRequest,
    service: AuthService = Depends(get_auth_service)
):
    return await service.forgot_password(request)

@router.post(
    "/reset-password",
    response_model=ResetPasswordResponse,
)
async def reset_password(
    request: ResetPasswordRequest,
    service: AuthService = Depends(
        get_auth_service
    ),
):
    return await service.reset_password(
        request
    )