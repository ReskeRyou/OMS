from typing import Any, Generic
from abc import ABC
from repository.core import Database
from repository.repo.base import BaseRepository, ModelType, SchemaType

class ServiceBase(Generic[ModelType, SchemaType], ABC):
    def __init__(self, db: Database, repository: type[BaseRepository[ModelType, SchemaType]]):
        self.db = db
        self.repo = repository

    async def get_all(self) -> list[SchemaType] | None:
        async with self.db.session_factory() as session:
            repo = self.repo(session=session)
            return await repo.get_all()

    async def get_by_id(self, _id: int) -> SchemaType | None:
        async with self.db.session_factory() as session:
            repo = self.repo(session=session)
            return await repo.get_by_id(_id)

    async def add(self, data: SchemaType) -> SchemaType | None:
        async with self.db.session_factory() as session:
            repo = self.repo(session=session)
            return await repo.add(data)

    async def update(self, data: SchemaType, _id: int) -> SchemaType | None:
        async with self.db.session_factory() as session:
            repo = self.repo(session=session)
            return await repo.update(data, _id)

    async def delete(self, _id: int) -> SchemaType | None:
        async with self.db.session_factory() as session:
            repo = self.repo(session=session)
            return await repo.delete(_id)

    async def get_by_field(self, field_name: str, value: Any) -> list[SchemaType] | None:
        async with self.db.session_factory() as session:
            repo = self.repo(session=session)
            return await repo.get_by_field(field_name, value)

    async def get_one_by_field(self, field_name: str, value: Any) -> SchemaType | None:
        async with self.db.session_factory() as session:
            repo = self.repo(session=session)
            return await repo.get_one_by_field(field_name, value)