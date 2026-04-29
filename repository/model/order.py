from dependency import *

class Order(Base):
    __tablename__ = 'orders'
    id : Mapped[int] = mapped_column('id', primary_key=True, autoincrement=True)
    user_id : Mapped[int] = mapped_column('user_id', nullable=False)
    status : Mapped[str] = mapped_column('status', nullable=False)
    created_at : Mapped[str] = mapped_column('created_at', nullable=False)