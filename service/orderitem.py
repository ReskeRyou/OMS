from main import db
from repository.model.orderItem import OrderItem as OrderItemModel
from dto.schema.orederltem import OrderItemSchema
from repository.repo.orderitem import OrderItemRepository
from service.core import ServiceBase


class OrderItemService(ServiceBase[OrderItemModel, OrderItemSchema]):
    def __init__(self):
        super().__init__(db=db, repository=OrderItemRepository)
