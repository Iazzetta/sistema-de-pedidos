from src.domains.product import Product


def test_should_create_product():
    product: Product = Product(
        name="PS5", description="O video game mais top (nem joguei)", price=5000
    )
    assert product.name == "PS5"
    assert product.description == "O video game mais top (nem joguei)"
    assert product.price == 5000.0
