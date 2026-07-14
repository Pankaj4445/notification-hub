from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.dependency import get_db
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.services.otp_service import OTPService
from app.services.email_service import EmailService
from app.security.jwt import JWTService
from app.core.config import settings

def get_email_service() -> EmailService:
    return EmailService(
        host=settings.SMTP_HOST,
        port=settings.SMTP_PORT,
        username=settings.SMTP_EMAIL,
        password=settings.SMTP_PASSWORD,
    )
def get_jwt_service() -> JWTService:
    return JWTService(
        secret_key=settings.SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
        access_token_expire_minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
    )
def get_auth_service(
    db: AsyncSession = Depends(get_db),
    email_service: EmailService = Depends(get_email_service),
    jwt_service: JWTService = Depends(get_jwt_service)
) -> AuthService:
    repository = UserRepository(db)
    otp_service = OTPService()
    return AuthService(repository, otp_service, email_service, jwt_service)


