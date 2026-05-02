from pydantic_settings import BaseSettings, SettingsConfigDict

class RepositoryBase(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "oms"
    DB_USER: str = "reske"
    DB_PASSWORD: str = ""
    DB_DEBUG: bool = False
    DB_POOL_SIZE: int = 10

    model_config = SettingsConfigDict(
        env_file=".env",
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