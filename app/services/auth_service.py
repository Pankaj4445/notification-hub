from app.exceptions.auth import (
    EmailAlreadyExistsException,
    InvalidCredentialsException,
    UserInactiveException,
    UsernameAlreadyExistsException,
    UserAlreadyVerifiedException,
    UserNotFoundException,
    UserNotVerifiedException,
    PasswordReuseException
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import ( 
    RegisterRequest,
    RegisterResponse,
    VerifyOTPRequest, 
    VerifyOTPResponse, 
    LoginRequest, 
    LoginResponse, 
    UserResponse,
    ForgotPasswordRequest,
    ForgotPasswordResponse,
    ResetPasswordRequest,
    ResetPasswordResponse
)
from app.security.password import hash_password, verify_password
from app.services.otp_service import OTPService
from app.services.notification_service import NotificationService
from app.security.jwt import JWTService


class AuthService:

    def __init__(
        self,
        user_repository: UserRepository,
        notification_service: NotificationService,
        jwt_service: JWTService,
        otp_service: OTPService,
    ):
        self.user_repository = user_repository
        self.otp_service = otp_service
        self.notification_service = notification_service
        self.jwt_service = jwt_service

    #verify_otp for activate user.
    async def verify_otp(
        self,
        request: VerifyOTPRequest,
    ) -> VerifyOTPResponse:
        
        user = await self.user_repository.get_by_email(request.email)
        if not user:
            raise UserNotFoundException()
        
        if user.is_verified:
            raise UserAlreadyVerifiedException()

        #verify_otp for actual check otp entered is correct or not
        await self.otp_service.verify_otp(
            purpose="register",
            email=user.email,
            otp=request.otp,
        )

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

        await self.notification_service.send_registration_otp(
            user.email,
        )
        
        return RegisterResponse(
            message="Registration successful.",
            email=user.email,
        )
    
    async def login(
        self,
        request: LoginRequest,
    ) -> LoginResponse:
        user = await self.user_repository.get_by_email(
            request.email
        )
        if not user:
            raise InvalidCredentialsException()
        if not user.is_verified:
            raise UserNotVerifiedException()
        
        if not verify_password(
            request.password,
            user.hashed_password,
        ):
            raise InvalidCredentialsException()
        
        if not user.is_active:
            raise UserInactiveException()
        
        access_token = self.jwt_service.create_access_token(
            user_id=user.id,
            email=user.email,
            role=user.role,
        )

        return LoginResponse(
            access_token=access_token,
            token_type="bearer",
            user=UserResponse.model_validate(user)
        )

    async def forgot_password(
        self,
        request: ForgotPasswordRequest,
    ) -> ForgotPasswordResponse:

        user = await self.user_repository.get_by_email(
            request.email
        )

        # Prevent email enumeration
        if not user:
            return ForgotPasswordResponse(
                message="If an account exists, a password reset OTP has been sent."
            )

        if not user.is_verified:
            return ForgotPasswordResponse(
                message="If an account exists, a password reset OTP has been sent."
            )

        await self.notification_service.send_password_reset_otp(
            user.email,
        )

        return ForgotPasswordResponse(
            message="If an account exists, a password reset OTP has been sent."
        )

    async def reset_password(
        self,
        request: ResetPasswordRequest,
    ) -> ResetPasswordResponse:
        user = await self.user_repository.get_by_email(
            request.email
        )

        if not user:
            raise UserNotFoundException()

        await self.otp_service.verify_otp(
            purpose="reset",
            email=user.email,
            otp=request.otp,
        )

        if verify_password(
            request.new_password,
            user.hashed_password,
        ):
            raise PasswordReuseException()

        hashed_password = hash_password(
            request.new_password
        )

        await self.user_repository.update_password(
            user,
            hashed_password,
        )

        return ResetPasswordResponse(
            message="Password reset successfully."
        )