import json

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_category():
    """Первая категория"""
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, " "200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
    )


@pytest.fixture
def second_category():
    """Вторая категория"""
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[
            Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7),
            Product('65" QLED 8K', "Система свет вокруг", 223000.0, 3),
        ],
    )


@pytest.fixture
def product():
    """Фикстура продукта"""
    return Product(name="Xiaomi Redmi Note 20", description="1024GB, Красный", price=63000.0, quantity=4)


@pytest.fixture
def temp_json_file(tmp_path):
    """Создает временный JSON-файл для тестов"""
    data = [
        {
            "name": "Смартфоны",
            "description": "Электроника",
            "products": [{"name": "Samsung Galaxy", "description": "256GB", "price": 50000.0, "quantity": 5}],
        }
    ]
    # Создаем папку data в переменной директории
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    file_path = data_dir / "products.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    return file_path
