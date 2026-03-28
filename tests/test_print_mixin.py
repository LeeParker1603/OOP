from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    Product(name="Xiaomi Redmi Note 20", description="1024GB, Красный", price=63000.0, quantity=4)

    message = capsys.readouterr()
    assert (
        message.out.strip() == "Smartphone('Iphone 15', '512GB, Gray space', 210000.0, 8)\n"
        "LawnGrass('Газонная трава', 'Элитная трава для газона', 500.0, 20)\n"
        "Product('Xiaomi Redmi Note 20', '1024GB, Красный', 63000.0, 4)"
    )
