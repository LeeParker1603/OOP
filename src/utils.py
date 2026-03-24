import json
import os

from src.category import Category
from src.product import Product


def load_json() -> list:
    """
    Загрузка json-файла
    """
    # Ищем файл настроек в разных местах
    possible_paths = [
        "data/products.json",
        "../data/products.json",
        os.path.join(os.path.dirname(__file__), "..", "data", "products.json"),
    ]

    for path in possible_paths:
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data
            except Exception:
                pass  # Игнорируем ошибки, переходим к следующему пути

    # Настройки по умолчанию
    return []


def create_objects_from_json(data: list) -> list:
    """
    Функция создания объектов из списка словарей после выгрузки json
    """

    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


# if __name__ == "__main__":
#     print(create_objects_from_json(load_json())[0].name)
#     print(create_objects_from_json(load_json())[0].products)
