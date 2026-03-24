class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, new_product):
        return cls(**new_product)


    @classmethod
    def new_product_with_check(cls, new_product: dict, existing_products: list):
        name = new_product.get('name')
        price = new_product.get('price')
        quantity = new_product.get('quantity')
        description = new_product.get('description', '')

        for existing_product in existing_products:
            if existing_product.name.lower() == name.lower():
                if price > existing_product.price:
                    existing_product.price = price

                existing_product.quantity += quantity

                if description and not existing_product.description:
                    existing_product.description = description

                return existing_product
        return cls(name, price, quantity, description)


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            print("Цена ниже предыдущей. Если вы уверены, введите y, если нет - n")
            while True:
                user_answer = str(input())
                if user_answer == "y":
                    self.__price = new_price
                    break
                if user_answer == "n":
                    print(f"Ввод новой цены отменен. Цена осталась прежняя {self.__price} руб.")
                    break
                else:
                    print("Введите ответ y/n")




