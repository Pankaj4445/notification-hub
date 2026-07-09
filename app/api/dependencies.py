from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.dependency import get_db
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.services.otp_service import OTPService

def get_auth_service(
    db: AsyncSession = Depends(get_db),
) -> AuthService:

    repository = UserRepository(db)
    otp_service = OTPService()
    return AuthService(repository, otp_service)