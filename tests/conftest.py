import json

import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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
def empty_category():
    """Фикстура с пустой категорией"""
    return Category("Электроника", "Компьютерная техника")


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


@pytest.fixture
def product_data():
    """Фикстура с данными в словаре"""
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture
def existing_product(product_data):
    """Фикстура с существующим продуктом (созданным из product_data)"""
    return Product.new_product(product_data)


@pytest.fixture
def duplicate_data():
    """Фикстура с данными для дубликата"""
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "price": 190000.0,  # Более высокая цена
        "quantity": 3,
        "description": "512GB, Черный цвет",
    }


@pytest.fixture
def new_product_data():
    """Фикстура с данными для нового продукта"""
    return {"name": "iPhone 15", "price": 210000.0, "quantity": 8, "description": "Новый iPhone"}


@pytest.fixture
def smartphone_product():
    """Фикстура смартфона"""
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone_product_2():
    """Фикстура смартфона 2"""
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawn_grass_product():
    """Фикстура травы газона"""
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass_product_2():
    """Фикстура травы газона 2"""
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
