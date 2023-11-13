from src.domains.base import DomainBase


class Product(DomainBase):
    name: str
    description: str
    price: float
