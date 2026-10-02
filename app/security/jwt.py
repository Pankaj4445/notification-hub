from uuid import UUID
from datetime import datetime, timedelta, timezone

import jwt
from jwt import (
    ExpiredSignatureError,
    InvalidTokenError,
)

from app.enums.user_role import UserRole
from app.exceptions.auth import TokenExpiredException, InvalidTokenException

class JWTService:

    def __init__(
        self,
        secret_key: str,
        algorithm: str,
        access_token_expire_minutes: int,
    ):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.access_token_expire_minutes = access_token_expire_minutes

    def create_access_token(
        self,
        user_id: UUID,
        email: str,
        role: UserRole,
    ) -> str:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=self.access_token_expire_minutes
        )
        payload = {
            "sub": str(user_id),
            "email": email,
            "role": role.value,
            "exp": expire,
        }

        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def decode_token(
        self,
        token: str,
    ) -> dict:

        try:
            payload = jwt.decode(
                token,
                self.secret_key,
                algorithms=[self.algorithm],
            )

            REQUIRED_CLAIMS = (
                "sub",
                "email",
                "role",
                "exp",
            )

            for claim in REQUIRED_CLAIMS:
                if claim not in payload:
                    raise InvalidTokenException()

            return payload

        except ExpiredSignatureError:
            raise TokenExpiredException()

        except InvalidTokenError:
            raise InvalidTokenException()