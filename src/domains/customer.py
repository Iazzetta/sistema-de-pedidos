from src.domains.base import DomainBase
from pydantic import BaseModel

class Customer(DomainBase):
    name: str
    email: str
    
class CustomerRegistration(BaseModel):
    name: str
    email: str
    password: str
    confirm_password: str
