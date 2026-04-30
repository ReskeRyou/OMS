from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config import repository_config
import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout  # Вывод в консоль
)


logger = logging.getLogger(__name__)


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
            logger.info(f"rollback exception: {exc_type}")
        await self.session.close()