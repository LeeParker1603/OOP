import os

from src.category import Category
from src.product import Product
from src.utils import create_objects_from_json, load_json


def test_load_json(temp_json_file, monkeypatch):
    """Тест загрузки данных из файла"""
    # Подменяем текущую рабочую директорию на временную, чтобы сработал путь 'data/products.json'
    monkeypatch.chdir(os.path.dirname(temp_json_file.parent))

    result = load_json()
    assert len(result) == 1
    assert result[0]["name"] == "Смартфоны"


def test_load_json_not_found(monkeypatch):
    """Тест поведения при отсутствии файла"""
    monkeypatch.setattr(os.path, "exists", lambda path: False)

    assert load_json() == []


def test_create_objects_from_json():
    """Тест преобразования словарей в объекты классов"""
    raw_data = [
        {
            "name": "Холодильники",
            "description": "Холодильное оборудование",
            "products": [{"name": "Бирюса", "description": "Двухкамерный", "price": 10000.0, "quantity": 10}],
        }
    ]

    categories = create_objects_from_json(raw_data)

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Холодильники"

    # Проверяем, что внутри категории объекты Product, а не словари
    assert len(categories[0].products) == 1
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].products[0].name == "Бирюса"
