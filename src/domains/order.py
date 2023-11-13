from uuid import UUID
from pydantic import BaseModel, Field
from src.domains.base import DomainBase
from enum import Enum

from src.domains.customer import Customer


class OrderStatusName(str, Enum):
    ACCOMPLISHED = "realizado"
    IN_PREPARATION = "em preparação"
    SENT = "enviado"
    DELIVERED = "entregue"
    FINISHED = "finalizado"


class OrderStatus(BaseModel):
    name: OrderStatusName = Field(default=OrderStatusName.ACCOMPLISHED)


class OrderItem(BaseModel):
    product_id: UUID
    price: float
    quantity: int


class Order(DomainBase):
    customer: Customer
    status: list[OrderStatus] = Field(default=[])
    items: list[OrderItem] = Field(default=[])

    def add_status(self, status: OrderStatus):
        self.status.append(status)

    def add_item(self, item: OrderItem):
        self.items.append(item)

    def total(self):
        return sum([item.price * item.quantity for item in self.items])
