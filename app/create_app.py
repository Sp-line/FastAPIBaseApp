from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

from core.models import database
from dependencies import InfrastructureProvider
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka as setup_fastapi_dishka
from fastapi import FastAPI

if TYPE_CHECKING:
    from collections.abc import AsyncIterator


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    yield
    await database.dispose()


def create() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    container = make_async_container(
        InfrastructureProvider(),
    )

    setup_fastapi_dishka(container, app)

    return app
