from repository.repo.base import BaseRepository
from repository.model.order import Order as OrderModel
from sqlalchemy.ext.asyncio import AsyncSession
from dto.schema.order import OrderSchema

class OrderRepository(BaseRepository[OrderModel, OrderSchema]):

    def __init__(self, session: AsyncSession):
        super().__init__(session, OrderModel, OrderSchema)