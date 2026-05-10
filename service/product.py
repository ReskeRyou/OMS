from main import db
from repository.model.product import Product as ProductModel
from dto.schema.product import ProductSchema
from repository.repo.product import ProductRepository
from service.core import ServiceBase


class ProductService(ServiceBase[ProductModel, ProductSchema]):
    def __init__(self):
        super().__init__(db=db, repository=ProductRepository)
