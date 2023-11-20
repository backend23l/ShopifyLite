from .product import Product


class Order:
    id = 1
    
    def __init__(self):
        self.order_id = Order.id
        self.products = []

    def add_product(self, product: Product, quantity: int) -> bool:
        if product.quantity > 0 and product.quantity >= quantity:
            self.products.append({
                "product": product,
                "quantity": quantity
            })

    def display(self) -> str:
        report = f"#{self.order_id} Your Order\n\n"

        count = 1
        total = 0
        for item in self.products:
            sub_total = item['product'].price * item['quantity']
            report += f"{count}. #{item['product'].product_id} {item['product'].name} {item['quantity']} X {item['product'].price} = {sub_total}\n"

            total += sub_total
            count += 1

        return report + f"\n\nTotal: {total}"
        