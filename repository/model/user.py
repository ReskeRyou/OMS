from .dependency import *

class User(Base):
    __tablename__ = "users"
    id : Mapped[int] = mapped_column('id', primary_key=True, autoincrement=True)
    email : Mapped[str] = mapped_column('email', nullable=False)
    hashed_password : Mapped[str] = mapped_column('hashed_password', nullable=False)
    role : Mapped[str] = mapped_column('role', nullable=False)