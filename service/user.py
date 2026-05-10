from main import db
from repository.model.user import User as UserModel
from dto.schema.user import UserSchema
from repository.repo.user import UserRepository
from service.core import ServiceBase


class UserService(ServiceBase[UserModel, UserSchema]):
    def __init__(self):
        super().__init__(db=db, repository=UserRepository)