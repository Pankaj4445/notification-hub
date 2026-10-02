import secrets

from app.redis.client import redis_client
from app.core.config import settings
from app.exceptions.auth import InvalidOTPException, UserAlreadyVerifiedException

class OTPService:

    def build_key(
        self,
        purpose: str,
        email: str,
    ) -> str:
        return f"otp:{purpose}:{email}"

    def generate_otp(self) -> str:
        return f"{secrets.randbelow(1_000_000):06d}"
    
    async def store_otp(
        self,
        purpose: str,
        email: str,
        otp: str,
    ):
        await redis_client.set(
            self.build_key(purpose,email),
            otp,
            ex=settings.OTP_EXPIRY_SECONDS
        )

    async def verify_otp(
        self,
        purpose: str,
        email: str,
        otp: str,
    ):
        key = self.build_key(purpose,email)
        stored_otp = await redis_client.get(key)
        if stored_otp is None:
            raise InvalidOTPException()
        elif stored_otp != otp:
            raise InvalidOTPException()
        await redis_client.delete(key)
        return True
    
    async def create_otp(
        self,
        purpose: str,
        email: str,
    ):
        otp = self.generate_otp()
        await self.store_otp(purpose,email, otp)
        return otp
        