from textwrap import dedent
from email.message import EmailMessage
import smtplib

from app.core.config import settings

class EmailService:

    def __init__(
        self,
        host: str,
        port: int,
        username: str,
        password: str
    ):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def _build_otp_subject(self) -> str:
        return "Notification Hub - Email Verification Code"
    
    def _build_otp_body(
        self,
        otp: str
    ) -> str:
        expiry_minutes = settings.OTP_EXPIRY_SECONDS // 60
        return dedent(f"""Hello,

Thank you for registering with Notification Hub.

Your verification code is:

{otp}

This OTP is valid for {expiry_minutes} minutes.

If you didn't request this, you can safely ignore this email.

Regards,
Notification Hub Team
""")
    
    async def send(
        self,
        to_email: str,
        subject: str,
        body: str
    ):
        msg = EmailMessage()

        msg["Subject"] = subject
        msg["From"] = self.username
        msg["To"] = to_email

        msg.set_content(body)

        with smtplib.SMTP(self.host, self.port) as server:
            server.starttls()
            server.login(self.username, self.password)
            server.send_message(msg)

    async def send_otp(
        self,
        email: str,
        otp: str
    ):
        subject = self._build_otp_subject()

        body = self._build_otp_body(otp)

        await self.send(
            to_email=email,
            subject=subject,
            body=body
        )