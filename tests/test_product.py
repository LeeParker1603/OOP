from unittest.mock import MagicMock

import pytest

from src.product import Product


def test_product_init(product):
    """Тест инициализации класса Product"""
    assert product.name == "Xiaomi Redmi Note 20"
    assert product.description == "1024GB, Красный"
    assert product.price == 63000.0
    assert product.quantity == 4


def test_new_product_init(product_data):
    """Тест создания продукта через класс-метод new_product"""
    new_product = Product.new_product(product_data)
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_new_product_with_check_new_product(product_data):
    """Тест создания нового продукта (дубликат не найден)"""
    existing_products = []
    new_product_data = {"name": "iPhone 15", "price": 210000.0, "quantity": 8, "description": "Новый iPhone"}

    new_product = Product.new_product_with_check(new_product_data, existing_products)

    assert isinstance(new_product, Product)
    assert new_product.name == "iPhone 15"
    assert new_product.price == 210000.0
    assert new_product.quantity == 8
    assert new_product.description == "Новый iPhone"


@pytest.mark.parametrize(
    "new_price,expected",
    [
        (200000, 200000),  # Повышение цены
        (180000, 180000),  # Такая же цена
    ],
)
def test_price_setter_higher_or_equal(product, new_price, expected):
    """Параметризованный тест повышения или сохранения цены"""
    product.price = new_price
    assert product.price == expected


@pytest.mark.parametrize("invalid_price", [0, -100, -5000])
def test_price_setter_invalid_price(product, invalid_price, capsys):
    """Параметризованный тест невалидных цен"""
    original_price = product.price
    product.price = invalid_price

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == original_price


def test_new_product_with_check_duplicate_lower_price_with_confirm(existing_product, monkeypatch, capsys):
    """Тест: установка более низкой цены с подтверждением 'y'"""
    monkeypatch.setattr("builtins.input", MagicMock(return_value="y"))

    existing_products = [existing_product]
    duplicate_data = {"name": existing_product.name, "price": 150000.0, "quantity": 2}  # Более низкая цена

    result = Product.new_product_with_check(duplicate_data, existing_products)

    assert result is existing_product
    assert result.price == 150000.0
    assert result.quantity == 7


def test_new_product_with_check_duplicate_lower_price_without_confirm(existing_product, monkeypatch, capsys):
    """Тест: установка более низкой цены без подтверждения 'n'"""
    monkeypatch.setattr("builtins.input", MagicMock(return_value="n"))

    existing_products = [existing_product]
    original_price = existing_product.price
    duplicate_data = {"name": existing_product.name, "price": 150000.0, "quantity": 2}

    result = Product.new_product_with_check(duplicate_data, existing_products)

    assert result is existing_product
    assert result.price == original_price  # Цена не должна измениться


def test_product__str__(product):
    assert str(product) == "Xiaomi Redmi Note 20, 63000.0 руб. Остаток 4 шт."


@pytest.mark.parametrize("price1, qty1, price2, qty2, expected", [
    (100.0, 10, 200.0, 5, 2000.0),
    (63000.0, 5, 55000.0, 12, 975000.0),
])
def test_product_add(price1, qty1, price2, qty2, expected):
    # Создаем два экземпляра продукта (замените Product на имя вашего класса)
    prod1 = Product("Товар 1", "Описание", price1, qty1)
    prod2 = Product("Товар 2", "Описание", price2, qty2)

    # Проверяем результат сложения
    assert prod1 + prod2 == expected
