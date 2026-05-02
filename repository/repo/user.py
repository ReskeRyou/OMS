from repository.repo.base import BaseRepository
from repository.model.user import User as UserModel
from dto.schema.user import UserSchema
from sqlalchemy.ext.asyncio import AsyncSession

class UserRepository(BaseRepository[UserModel, UserSchema]):

    def __init__(self, session: AsyncSession):
        super().__init__(session, UserModel, UserSchema)