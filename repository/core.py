import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import select
from asyncpg.exceptions import UndefinedColumnError
from sqlalchemy.exc import ProgrammingError
import logging

class DataBase:
    from dotenv import load_dotenv
    load_dotenv()
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_DATABASE")
    debug = os.getenv("DB_DEBUG")

    engine = None

    def __init__(self, user=user, password=password, host=host,database=database, port=port, debug=debug):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.dbname = database
        self.debug = (True if debug == 1 else False)
        url = f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"
        self.engine = create_async_engine(
            url=url,
            echo=self.debug,
            pool_size=10,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    async def get_all(self, table):
        try:
            async with self.session_factory() as session:
                res = await session.execute(select(table))
                return res.scalars().all()
        except ProgrammingError as e:
            if "UndefinedColumnError" in str(e):
                logging.error(f"Column {table.__name__} not defined")
                return []
            else:
                logging.error(f"ProgrammingError: {e}")
                raise e

db = DataBase()

async def main():
    from model.user import User
    await db.get_all(User)

if __name__ == "__main__":
    asyncio.run(main())