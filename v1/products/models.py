from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg

from uuid import UUID, uuid4
from datetime import datetime


class Product(SQLModel, table=True):
    __tablename__ = "products"

    id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid4
        )
    )
    name: str
    description: str
    price: float
    stock: int

    created_at: datetime = Field(sa_column=Column(
        pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(
        pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f"<Product {self.name}>"
