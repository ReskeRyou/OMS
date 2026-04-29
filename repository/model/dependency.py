from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import Column, String, Integer, ForeignKey

class Base(DeclarativeBase):
    ...