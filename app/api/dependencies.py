from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.dependency import get_db
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.services.otp_service import OTPService
from app.services.email_service import EmailService
from app.security.jwt import JWTService
from app.services.notification_service import NotificationService
from app.core.config import settings

def get_email_service() -> EmailService:
    return EmailService(
        host=settings.SMTP_HOST,
        port=settings.SMTP_PORT,
        username=settings.SMTP_EMAIL,
        password=settings.SMTP_PASSWORD,
    )

def get_otp_service() -> OTPService:
    return OTPService()

def get_jwt_service() -> JWTService:
    return JWTService(
        secret_key=settings.SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
        access_token_expire_minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
    )

def get_notification_service(
    otp_service: OTPService = Depends(get_otp_service),
    email_service: EmailService = Depends(get_email_service),
) -> NotificationService:
    return NotificationService(
        otp_service=otp_service,
        email_service=email_service,
    )

def get_user_repository(
    db: AsyncSession = Depends(get_db),
        ) -> UserRepository:
    return UserRepository(db)

def get_auth_service(
    user_repository: UserRepository = Depends(get_user_repository),
    notification_service: NotificationService = Depends(get_notification_service),
    jwt_service: JWTService = Depends(get_jwt_service),
    otp_service: OTPService = Depends(get_otp_service),
) -> AuthService:
    return AuthService(user_repository, notification_service, jwt_service, otp_service)