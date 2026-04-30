from dto.dependency import PydanticBase

class OrderSchema(PydanticBase):
    id: int | None = None
    user_id: int | None = None
    status: str | None = None
    created_at: str | None = None