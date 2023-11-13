from src.domains.customer import CustomerRegistration, Customer
from src.datalayer.base import RepositoryInterface

class CustomerRepositoryInterface(RepositoryInterface):
    
    async def register(self, customer_registration: CustomerRegistration) -> Customer:
        raise NotImplementedError
    
    async def email_already_exists(self, email: str) -> bool:
        raise NotImplementedError