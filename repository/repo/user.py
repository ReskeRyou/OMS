from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update
from repository.model.user import User
from repository.exception import RepositoryException
from dto.schema.user import UserSchema

class UserRepository:


    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_all(self) -> list[UserSchema] | None:
        query = await self.session.execute(select(User))
        result = query.scalars().all()
        return [UserSchema.model_validate(user) for user in result]


    async def get_by_id(
            self,
            _id : int
    ) -> UserSchema | None:

        query = select(User).where(User.id == _id)
        result = await self.session.execute(query)

        try:
            return UserSchema.model_validate(
                result.scalar_one_or_none()
            )
        except:
            raise RepositoryException("user by id not found")


    async def get_by_email(
            self,
            email : str
    ) -> UserSchema | None:

        query = await self.session.execute(select(User).where(User.email == email))
        result = query.scalars().first()
        return UserSchema.model_validate(result)


    async def get_by_role(
            self,
            role : str
    ) -> list[UserSchema] | None:

        query = await self.session.execute(select(User).where(User.role == role))
        result = query.scalars().all()
        return [UserSchema.model_validate(user) for user in result]

    async def add_user(
            self,
            user : UserSchema
    ) -> UserSchema | None:
        stmt = insert(User).values(
            **user.model_dump(exclude={"id"},
                              exclude_none=True
                              )).returning(User)

        result = await self.session.execute(stmt)
        created_user = result.scalar_one()
        await self.session.commit()
        return UserSchema.model_validate(created_user)


    async def update_user(
            self,
            user : UserSchema,
            _id : int
    ) -> UserSchema | None:

        stmt = (update(User).values(
            **user.model_dump(
                exclude={"id"},
                exclude_none=True
            )
        ).where(User.id == _id)).returning(User)

        result = await self.session.execute(stmt)
        updated_user = result.scalar_one_or_none()
        await self.session.commit()
        return UserSchema.model_validate(updated_user)