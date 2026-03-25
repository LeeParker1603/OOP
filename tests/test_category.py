import pytest

from src.category import Category
from src.product import Product


def test_category_init(first_category, second_category):
    """Тест инициализации класса Category"""
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )

    products_list = first_category.get_products_list()
    assert len(products_list) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_category_init_empty():
    """Тест инициализации пустой категории"""
    category = Category("Электроника", "Компьютерная техника")

    assert category.name == "Электроника"
    assert category.description == "Компьютерная техника"
    assert category.get_products_list() == []


def test_products_property_empty(empty_category):
    """Тест свойства products для пустой категории"""
    result = empty_category.products
    assert result == ""


def test_products_property_with_products(first_category):
    """Тест свойства products с товарами"""
    result = first_category.products

    assert "Samsung Galaxy S23 Ultra" in result
    assert "Iphone 15" in result
    assert "180000.0" in result
    assert "210000.0" in result
    assert "5" in result
    assert "8" in result


@pytest.mark.parametrize(
    "products,expected",
    [
        # (список товаров в формате (name, price, quantity), ожидаемый вывод)
        ([("Ноутбук", 50000, 10)], "Ноутбук, 50000 руб. Остаток: 10 шт.\n"),
        ([("Мышь", 1500, 50)], "Мышь, 1500 руб. Остаток: 50 шт.\n"),
        ([("Клавиатура", 3000, 25)], "Клавиатура, 3000 руб. Остаток: 25 шт.\n"),
        ([("Монитор", 25000, 7)], "Монитор, 25000 руб. Остаток: 7 шт.\n"),
        (
            [("Ноутбук", 50000, 10), ("Мышь", 1500, 50)],
            "Ноутбук, 50000 руб. Остаток: 10 шт.\nМышь, 1500 руб. Остаток: 50 шт.\n",
        ),
        (
            [("Ноутбук", 50000, 10), ("Мышь", 1500, 50), ("Клавиатура", 3000, 25)],
            "Ноутбук, 50000 руб. Остаток: 10 шт.\nМышь, 1500 руб. Остаток: 50 шт.\nКлавиатура, 3000 руб. Остаток: 25 шт.\n",
        ),
        (
            [("Телефон", 50000, 5), ("Телефон", 55000, 3)],
            "Телефон, 50000 руб. Остаток: 5 шт.\nТелефон, 55000 руб. Остаток: 3 шт.\n",
        ),
        ([], ""),  # Пустая категория
    ],
)
def test_products_property_format_compact(empty_category, products, expected):
    """Компактный параметризованный тест форматирования свойства products"""
    for name, price, quantity in products:
        product = Product(name, "", price, quantity)
        empty_category.add_product(product)

    assert empty_category.products == expected


def test_category__str__(first_category):
    assert str(first_category) == "Смартфоны, количество продуктов: 13 шт."
