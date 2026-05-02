from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class RepositoryBase(BaseSettings):
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432
    DB_NAME: str = 'postgres'
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = ''
    DB_DEBUG: bool = False
    DB_POOL_SIZE: int = 5

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / '.env.development',
        env_file_encoding="utf-8",
        extra='ignore'
    )

    @property
    def engine_kwargs(self):
        return {
            "url" : f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}",
            "echo" : self.DB_DEBUG,
            "pool_size" : self.DB_POOL_SIZE,
        }

repository_config = RepositoryBase()