from dependency import *

class Product(Base):
    __tablename__ = 'products'
    id : Mapped[int] = mapped_column('id', primary_key=True,autoincrement=True)
    name : Mapped[str] = mapped_column('name', nullable=False)
    price : Mapped[float] = mapped_column('price', nullable=False)
    stock_quantity : Mapped[int] = mapped_column('stock_quantity', nullable=False)