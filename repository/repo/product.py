from repository.repo.base import BaseRepository
from repository.model.product import Product as ProductModel
from sqlalchemy.ext.asyncio import AsyncSession
from dto.schema.product import ProductSchema

class ProductRepository(BaseRepository[ProductModel, ProductSchema]):

    def __init__(self, session: AsyncSession):
        super().__init__(session, ProductModel, ProductSchema)