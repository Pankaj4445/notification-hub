from app.exceptions.auth import (
    EmailAlreadyExistsException,
    UsernameAlreadyExistsException,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import RegisterRequest, RegisterResponse
from app.security.password import hash_password


class AuthService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

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

        return RegisterResponse(
            message="Registration successful.",
            email=user.email,
        )