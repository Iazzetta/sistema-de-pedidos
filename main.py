from src.factories.customer_factory import CustomerFactory
from src.domains.customer import CustomerRegistration

service = CustomerFactory.create_mock()

customer = CustomerRegistration(
    name = "Guilherme",
    email = "gui@gui.com",
    password = "123456",
    confirm_password = "123456",
)

response = await service.register(customer_registration=customer)

print(response)