from dto.schema.orederltem import OrderItemSchema
from repository.repo.base import BaseRepository
from repository.model.orderItem import OrderItem as OrderItemModel
from sqlalchemy.ext.asyncio import AsyncSession

class ProductRepository(BaseRepository[OrderItemModel, OrderItemSchema]):

    def __init__(self, session: AsyncSession):
        super().__init__(session, OrderItemModel, OrderItemSchema)