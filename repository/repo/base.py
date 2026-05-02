from typing import TypeVar, Generic, Type, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, delete
from pydantic import BaseModel
from repository.exception import RepositoryException

ModelType = TypeVar("ModelType")
SchemaType = TypeVar("SchemaType", bound=BaseModel)


class BaseRepository(Generic[ModelType, SchemaType]):

    def __init__(
            self,
            session: AsyncSession,
            model: Type[ModelType],
            schema: Type[SchemaType]
    ):
        self.session = session
        self.model = model
        self.schema = schema

    async def get_all(self) -> list[SchemaType] | None:
        query = await self.session.execute(select(self.model))
        result = query.scalars().all()
        return [self.schema.model_validate(item) for item in result]

    async def get_by_id(self, _id: int) -> SchemaType | None:
        query = select(self.model).where(self.model.id == _id)
        result = await self.session.execute(query)

        try:
            return self.schema.model_validate(result.scalar_one_or_none())
        except Exception:
            raise RepositoryException(f"{self.model.__name__} by id not found")

    async def add(self, data: SchemaType) -> SchemaType | None:
        stmt = insert(self.model).values(
            **data.model_dump(
                exclude={"id"},
                exclude_none=True
            )
        ).returning(self.model)

        result = await self.session.execute(stmt)
        created = result.scalar_one()
        await self.session.commit()
        return self.schema.model_validate(created)

    async def update(self, data: SchemaType, _id: int) -> SchemaType | None:
        stmt = (update(self.model).values(
            **data.model_dump(
                exclude={"id"},
                exclude_none=True
            )
        ).where(self.model.id == _id)).returning(self.model)

        result = await self.session.execute(stmt)
        updated = result.scalar_one_or_none()
        await self.session.commit()
        return self.schema.model_validate(updated)

    async def delete(self, _id: int) -> SchemaType | None:
        stmt = (delete(self.model).where(self.model.id == _id)).returning(self.model)
        result = await self.session.execute(stmt)
        deleted = result.scalar_one_or_none()
        await self.session.commit()
        return self.schema.model_validate(deleted)

    async def get_by_field(self, field_name: str, value: Any) -> list[SchemaType] | None:
        field = getattr(self.model, field_name, None)
        if not field:
            raise RepositoryException(f"Field {field_name} not found in model")

        query = await self.session.execute(select(self.model).where(field == value))
        result = query.scalars().all()
        return [self.schema.model_validate(item) for item in result]

    async def get_one_by_field(self, field_name: str, value: Any) -> SchemaType | None:
        field = getattr(self.model, field_name, None)
        if not field:
            raise RepositoryException(f"Field {field_name} not found in model")

        query = await self.session.execute(select(self.model).where(field == value))
        result = query.scalars().first()
        return self.schema.model_validate(result) if result else None