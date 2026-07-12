from fastapi import APIRouter, Depends

from app.api.dependencies import get_auth_service
from app.schemas.auth import RegisterRequest, RegisterResponse, VerifyOTPRequest, VerifyOTPResponse
from app.services.auth_service import AuthService

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