from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user_sessions import UserSession


class SessionRepository:

    def __init__(
        self,
        db: AsyncSession,
    ):
        self.db = db

    async def create_session(
        self,
        session: UserSession,
    ) -> UserSession:

        self.db.add(session)

        await self.db.commit()
        await self.db.refresh(session)

        return session

    async def get_by_token_hash(
        self,
        token_hash: str,
    ) -> UserSession | None:

        result = await self.db.execute(
            select(UserSession).where(
                UserSession.refresh_token_hash == token_hash
            )
        )

        return result.scalar_one_or_none()

    async def revoke_session(
        self,
        session: UserSession,
    ) -> UserSession:

        session.revoked_at = datetime.now()

        await self.db.commit()
        await self.db.refresh(session)

        return session

    async def revoke_all_user_sessions(
        self,
        user_id: UUID,
    ) -> None:

        await self.db.execute(
            update(UserSession)
            .where(
                UserSession.user_id == user_id,
                UserSession.revoked_at.is_(None),
            )
            .values(
                revoked_at=datetime.now()
            )
        )

        await self.db.commit()