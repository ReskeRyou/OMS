from dto.dependency import *

class UserSchema(PydanticBase):
    id: int | None = None
    email: EmailStr | None = None
    hashed_password: str | None = None
    role: str | None = None