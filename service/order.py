from main import db
from repository.model.order import Order as OrderModel
from dto.schema.order import OrderSchema
from repository.repo.order import OrderRepository
from service.core import ServiceBase


class OrderService(ServiceBase[OrderModel, OrderSchema]):
    def __init__(self):
        super().__init__(db=db, repository=OrderRepository)
