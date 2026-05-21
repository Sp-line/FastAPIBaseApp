from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

from contextlib import asynccontextmanager

import uvicorn
from api import router
from core.config import settings
from core.models import database
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    yield
    await database.dispose()


app = FastAPI(
    lifespan=lifespan,
)
app.include_router(
    router,
    prefix=settings.api.prefix,
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
