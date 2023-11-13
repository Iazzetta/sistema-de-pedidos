from src.domains.customer import Customer


def test_should_create_customer():
    customer: Customer = Customer(name="Guilherme", email="gui@gui.com")

    assert customer.name == "Guilherme"
    assert customer.email == "gui@gui.com"
