def test_product_init(product):
    """Тест инициализации класса Product"""
    assert product.name == "Xiaomi Redmi Note 20"
    assert product.description == "1024GB, Красный"
    assert product.price == 63000.0
    assert product.quantity == 4
