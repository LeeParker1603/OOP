import pytest


def test_smartphone_init(smartphone_product):
    """Тест инициализации класса Smartphone(Product)"""
    assert smartphone_product.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_product.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_product.price == 180000.0
    assert smartphone_product.quantity == 5
    assert smartphone_product.efficiency == 95.5
    assert smartphone_product.model == "S23 Ultra"
    assert smartphone_product.memory == 256
    assert smartphone_product.color == "Серый"


def test_smartphone_add(smartphone_product, smartphone_product_2):
    assert smartphone_product + smartphone_product_2 == 2580000


def test_smartphone_add_error(smartphone_product, lawn_grass_product):
    with pytest.raises(TypeError):
        result = smartphone_product + lawn_grass_product
