from dependency import *

class OrderItem(Base):
    order_id : Mapped[int] = mapped_column('order_id', nullable=False)
    product_id : Mapped[int] = mapped_column('order_item', nullable=False)
    quantity : Mapped[int] = mapped_column('quantity', nullable=False)
    price_at_purchase : Mapped[float] = mapped_column('price', nullable=False)