import uvicorn
from api import router
from core.config import settings
from create_app import create

app = create()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
