from dto.dependency import *

class Product(PydanticBase):
    id : int | None = None
    name : str = Field(max_length=20)
    price : float | None = None
    stock_quantity : int | None = None