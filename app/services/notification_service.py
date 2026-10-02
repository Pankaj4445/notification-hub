from app.services.email_service import EmailService
from app.services.otp_service import OTPService


class NotificationService:

    def __init__(
        self,
        otp_service: OTPService,
        email_service: EmailService,
    ):
        self.otp_service = otp_service
        self.email_service = email_service

    async def send_registration_otp(
        self,
        email: str,
    ) -> None:
        otp = await self.otp_service.create_otp(
            purpose="register",
            email=email,
        )

        subject = "Notification Hub - Email Verification"

        body = f"""
Hello,

Your verification code is:

{otp}

Regards,
Notification Hub
"""

        await self.email_service.send(
            to_email=email,
            subject=subject,
            body=body,
        )

    async def send_password_reset_otp(
        self,
        email: str,
    ) -> None:

        otp = await self.otp_service.create_otp(
            purpose="reset",
            email=email,
        )

        subject = "Notification Hub - Password Reset"

        body = f"""
    Hello,

    You requested to reset your password.

    Your OTP is:

    {otp}

    If you didn't request this, please ignore this email.

    Regards,
    Notification Hub Team
    """

        await self.email_service.send(
            to_email=email,
            subject=subject,
            body=body,
        )