from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from collections.abc import Callable

from app.repositories.user_repository import UserRepository
from app.models.user import User
from app.enums.user_role import UserRole
from app.security.jwt import JWTService
from app.api.dependencies import get_jwt_service, get_user_repository
from app.exceptions.auth import InvalidTokenException, UserInactiveException, PermissionDeniedException


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
)


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    jwt_service: JWTService = Depends(get_jwt_service),
    user_repository: UserRepository = Depends(get_user_repository),
):
    payload = jwt_service.decode_token(token)
    user_id = payload["sub"]
    user = await user_repository.get_by_userid(user_id)
    if not user:
        raise InvalidTokenException()
    if not user.is_active:
        raise UserInactiveException()
    return user


def require_role(
    *roles: UserRole,
) -> Callable:
    async def role_checker(
        current_user: User = Depends(get_current_user),
    ) -> User:

        if current_user.role not in roles:
            raise PermissionDeniedException()

        return current_user

    return role_checker