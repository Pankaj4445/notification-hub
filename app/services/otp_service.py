import secrets

from app.redis.client import redis_client
from app.core.config import settings

class OTPService:

    def register_otp_key(self,email: str) -> str:
        return f"register_otp:{email}"

    def generate_otp(self) -> str:
        return f"{secrets.randbelow(1_000_000):06d}"
    
    async def store_otp(self, email: str, otp: str):
        await redis_client.set(
            self.register_otp_key(email),
            otp,
            ex=settings.OTP_EXPIRY_SECONDS
        )

    async def verify_otp(self, email: str, otp: str) -> bool:
        key = self.register_otp_key(email)
        stored_otp = await redis_client.get(key)
        if stored_otp is None:
            return False
        elif stored_otp != otp:
            return False
        await redis_client.delete(key)
        return True
    
    async def create_otp(self, email: str) -> str:
        otp = self.generate_otp()
        await self.store_otp(email, otp)
        return otp
        