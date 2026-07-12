from app.exceptions.auth import (
    EmailAlreadyExistsException,
    UsernameAlreadyExistsException,
    UserAlreadyVerifiedException,
    UserNotFoundException,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import RegisterRequest, RegisterResponse, VerifyOTPRequest, VerifyOTPResponse
from app.security.password import hash_password
from app.services.otp_service import OTPService
from app.services.email_service import EmailService


class AuthService:

    def __init__(self, user_repository: UserRepository, otp_service: OTPService,email_service: EmailService):
        self.user_repository = user_repository
        self.otp_service = otp_service
        self.email_service = email_service

    async def verify_otp(
        self,
        request: VerifyOTPRequest,
    ) -> VerifyOTPResponse:
        
        user = await self.user_repository.get_by_email(request.email)
        if not user:
            raise UserNotFoundException()
        
        if user.is_verified:
            raise UserAlreadyVerifiedException()
        
        await self.otp_service.verify_otp(user.email, request.otp)

        await self.user_repository.activate_user(user)

        return VerifyOTPResponse(
            message="OTP verified successfully."
        )

    async def register(
        self,
        request: RegisterRequest,
    ) -> RegisterResponse:

        existing_email = await self.user_repository.get_by_email(
            request.email
        )

        if existing_email:
            raise EmailAlreadyExistsException()

        existing_username = await self.user_repository.get_by_username(
            request.username
        )

        if existing_username:
            raise UsernameAlreadyExistsException()

        user = User(
            username=request.username,
            email=request.email,
            first_name=request.first_name,
            last_name=request.last_name,
            hashed_password=hash_password(request.password),
        )

        await self.user_repository.create_user(user)

        otp = await self.otp_service.create_otp(user.email)

        await self.email_service.send_otp(
            email=user.email,
            otp=otp
        )
        
        return RegisterResponse(
            message="Registration successful.",
            email=user.email,
        )