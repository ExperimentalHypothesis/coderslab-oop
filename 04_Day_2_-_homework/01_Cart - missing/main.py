from uuid import uuid4


class Product:
    last = 1

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        self.id = Product.last
        Product.last += 1

    def __repr__(self):
        return f"Product({self.name}, {self.price})"


class ShoppingCart:
    def __init__(self):
        self.products = {}  # id: Product
        self.quantities = {}  # id: qry

    def add_product(self, product: Product):
        self.products[product.id] = product
        self.quantities[product.id] = self.quantities.get(product.id, 0) + 1

    def remove_product(self, product: Product):
        self.products.pop(product.id, None)
        self.quantities.get(product.id, 0) - 1

    def change_product_qty(self, product: Product, new_qty: int):
        if new_qty < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantities[product.id] = new_qty
        if new_qty == 0:
            self.products.pop(product.id)

    def get_receipt(self):
        lines = []
        total = 0
        for id_, product in self.products.items():
            price = product.price
            qty = self.quantities[id_]
            sub_total = price * qty
            total += sub_total
            lines.append(f"{product.name} - quantity {qty}, price: {price} EUR, total: {sub_total} EUR\n")
        lines.append(f"Total: {total} EUR")

        return "".join(lines)


if __name__ == "__main__":
    bread = Product('Bread', 2.70)
    ham = Product('Ham', 8.40)
    cheese = Product('Cheese', 4.40)
    chives = Product('Chives', 1.50)
    pepper = Product('Pepper', 2.35)

    cart = ShoppingCart()
    print(cart.products)
    print(cart.quantities)
    print(cart.get_receipt())
    cart.add_product(bread)
    cart.add_product(bread)
    cart.add_product(bread)
    cart.add_product(pepper)
    cart.add_product(chives)

    cart.change_product_qty(pepper, 2)
    print(cart.products)
    print(cart.quantities)

    cart.remove_product(bread)
    print(cart.get_receipt())
