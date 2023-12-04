import config_api
import contextlib
from typing import AsyncIterator
from fastapi import FastAPI

from api.api_views import user_router


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    config_api.db_manager.init(config_api.settings.database_url)
    yield
    await config_api.db_manager.close()


app = FastAPI(title="Money API", lifespan=lifespan)

app.include_router(user_router, prefix="/api", tags=["/api"])
