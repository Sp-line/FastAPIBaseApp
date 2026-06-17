from __future__ import annotations

from typing import TYPE_CHECKING

from core.models import database
from dishka import Provider
from dishka import Scope
from dishka import provide

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

    from sqlalchemy.ext.asyncio import AsyncSession


class InfrastructureProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_db_session(self) -> AsyncIterator[AsyncSession]:
        async with database.session_factory() as session:
            yield session
