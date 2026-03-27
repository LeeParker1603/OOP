def test_lawn_grass_product_init(lawn_grass_product):
    """Тест инициализации класса LawnGrass(Product)"""
    assert lawn_grass_product.name == "Газонная трава"
    assert lawn_grass_product.description == "Элитная трава для газона"
    assert lawn_grass_product.price == 500.0
    assert lawn_grass_product.quantity == 20
    assert lawn_grass_product.country == "Россия"
    assert lawn_grass_product.germination_period == "7 дней"
    assert lawn_grass_product.color == "Зеленый"


def test_lawn_grass_product_add(lawn_grass_product, lawn_grass_product_2):
    assert lawn_grass_product + lawn_grass_product_2 == 16750
