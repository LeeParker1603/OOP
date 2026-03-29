import pytest

from src.exceptions import ZeroProductQuantityException
from src.order import Order
from src.product import Product


def test_order_init(order):
    """Тест инициализации класса Order"""
    assert order.name == "Заказ #1"
    assert order.description == "Покупка смартфона"
    assert order.products.name == "Xiaomi Redmi Note 20"
    assert order.quantity == 2


@pytest.mark.parametrize(
    "invalid_product",
    [
        [Product("Товар1", "", 100, 5), Product("Товар2", "", 200, 3)],  # список
        (Product("Товар1", "", 100, 5), Product("Товар2", "", 200, 3)),  # кортеж
        "не товар",  # строка
        123,  # число
        None,  # None
        {"name": "Ноутбук"},  # словарь
        [Product("Товар1", "", 100, 5)],  # список с одним товаром
    ],
)
def test_order_invalid_product_types(product, invalid_product):
    """Тест: все неверные типы вызывают ошибку"""
    with pytest.raises(TypeError, match="В заказе может быть только объект класса Product"):
        Order("Заказ #1", "Покупка", invalid_product, 2)


def test_order_negative_quantity(product):
    with pytest.raises(ZeroProductQuantityException, match="Количество должно быть больше нуля"):
        Order("Заказ #1", "Покупка", product=product, quantity=(-2))


def test_order_get_info(order, capsys):
    print(order)

    message = capsys.readouterr()
    assert (
        message.out.strip() == "Заказ: Заказ #1\n"
        "Описание: Покупка смартфона\n"
        "Товар: Xiaomi Redmi Note 20\n"
        "Количество: 2 шт.\n"
        "Итоговая стоимость: 126000.0 руб."
    )
