from core.config import settings
from fastapi import APIRouter

router = APIRouter(
    prefix=settings.api.prefix,
)
