from dto.dependency import *

class OrderItemSchema(PydanticBase):
    order_id: int | None = None
    product_id: int | None = None
    quantity: int | None = None
    price_at_purchase: float | None = None