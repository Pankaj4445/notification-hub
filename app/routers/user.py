from fastapi import APIRouter, Depends

from app.security.dependencies import require_role
from app.models.user import User
from app.enums.user_role import UserRole

router = APIRouter(
    prefix="/user",
    tags=["User"],
)

@router.get("/dashboard")
async def dashboard(
    current_user: User = Depends(
        require_role(
            UserRole.USER,
            UserRole.ADMIN,
        )
    ),
):
    return {
        "message": "Welcome User",
        "user": current_user.username,
    }