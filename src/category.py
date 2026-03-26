from src.product import Product


class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.product_count += len(products) if products else 0
        Category.category_count += 1

    def __str__(self):
        sum_products = 0
        for product in self.__products:
            sum_products += product.quantity
        return f"{self.name}, количество продуктов: {sum_products} шт."

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    def get_products_list(self):
        return self.__products.copy()

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1
