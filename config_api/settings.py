from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

from config_api.conf import *


class Settings(BaseSettings):

    database_url: str = "postgresql+asyncpg://postgres:password@localhost:5432/money_db"

    project_root: Path = Path(__file__).parent.parent.resolve()

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
