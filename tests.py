from src.product import Product
from src.order import Order

p1 = Product(name='Samsung s21', price=780.60, quantity=78)
p2 = Product(name='Iphone 12', price=400.30, quantity=89)
p3 = Product(name='Readme 14', price=450.00, quantity=63)


order1 = Order( )
order1.add_product(p1, 7)
order1.add_product(p2, 13)
order1.add_product(p3, 2)

print(order1.display())