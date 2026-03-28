from src.base_action import Action
from src.product import Product


class Order(Action):

    order_count = 0

    def __init__(self, name, description, product, quantity):
        super().__init__(name, description)

        if not isinstance(product, Product):
            raise TypeError("В заказе может быть только объект класса Product")
        self._product = product
        self.quantity = quantity
        self._total_price = self._calculate_total_price()

        Order.order_count += 1

    @property
    def products(self) -> Product:
        """Геттер для товара"""
        return self._product

    @products.setter
    def products(self, value: Product):
        """Сеттер для товара (пересчитываем итоговую стоимость)"""
        self._product = value
        self._total_price = self._calculate_total_price()

    @property
    def quantity(self) -> int:
        """Геттер для количества"""
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        """Сеттер для количества (пересчитывает итоговую стоимость)"""
        if value <= 0:
            raise ValueError("Количество должно быть больше нуля")
        self._quantity = value
        self._total_price = self._calculate_total_price()

    @property
    def total_price(self) -> float:
        """Геттер для итоговой стоимости"""
        return self._total_price

    def _calculate_total_price(self) -> float:
        """Приватный метод для расчета итоговой стоимости"""
        if self._product and self._quantity:
            return self._product.price * self._quantity
        return 0.0

    def get_info(self) -> str:
        """Информация о заказе"""
        return (
            f"Заказ: {self.name}\n"
            f"Описание: {self.description}\n"
            f"Товар: {self._product.name}\n"
            f"Количество: {self._quantity} шт.\n"
            f"Итоговая стоимость: {self._total_price} руб."
        )

    def confirm(self) -> bool:
        """Подтверждение заказа (уменьшает количество товара на складе)"""

        if self._product.quantity < self._quantity:
            raise ValueError(f"Недостаточно товара на складе. Доступно: {self._product.quantity} шт.")

        # Уменьшаем количество товара на складе
        self._product.quantity -= self._quantity
        print(f"Заказ '{self.name}' подтвержден! Списано {self._quantity} шт. товара '{self._product.name}'")
        return True

    def __str__(self) -> str:
        return self.get_info()

    def __repr__(self) -> str:
        return f"Order({self.name}, {self.products.name}, {self.quantity}," f" {self.total_price})"
