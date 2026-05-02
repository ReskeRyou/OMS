from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from .config import repository_config
from .exception import RepositoryException

class Database:

    def __init__(self):
        self.engine = create_async_engine(
            **repository_config.engine_kwargs
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    async def __aenter__(self):
        self.session = self.session_factory()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.session.rollback()
        await self.session.close()