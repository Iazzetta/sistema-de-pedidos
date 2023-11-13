from src.datalayer.repositories.mock.memdb import CUSTOMER_DB
from src.factories.customer_factory import CustomerFactory
from src.domains.customer import CustomerRegistration
from src.services.exceptions.customer_exceptions import EmailAlreadyExist
import pytest

@pytest.mark.asyncio
async def test_should_create_customer():

    service = CustomerFactory.create_mock()

    customer = CustomerRegistration(
        name = "Guilherme",
        email = "gui@gui.com",
        password = "123456",
        confirm_password = "123456",
    )

    response = await service.register(customer_registration=customer)
    print(response)
    
    
@pytest.mark.asyncio
async def test_should_raise_error_when_create_customer():

    service = CustomerFactory.create_mock()

    customer_duplicated = CustomerRegistration(
        name = "Guilherme",
        email = "gui@gui.com",
        password = "123456",
        confirm_password = "123456",
    )

    with pytest.raises(EmailAlreadyExist) as error:
        await service.register(customer_registration=customer_duplicated)
    
    assert str(error.value) == "E-mail already exists"
    
    