class Product:
    id = 1

    def __init__(self, name: str, price: float, quantity: int):
        self.product_id = Product.id
        self.name = name
        self.price = price
        self.quantity = quantity

        Product.id += 1

    def info(self) -> str:
        return f"{self.product_id}. {self.name}"