import copy


class Cart:
    def __init__(self):
        self.products = []

    def add(self, price: int | float, name: str):
        self.products.append((price, name))

    def summary(self):
        return self.products


class Discount20PercentCart(Cart):
    def summary(self):
        return [(price * 0.8, product) for price, product in self.products]


class Above3ProductsCheapestFreeCart(Cart):
    def summary(self):
        products = copy.deepcopy(self.products)
        if len(products) > 3:
            cheapest = min(products, key=lambda x: x[0])
            products.remove(cheapest)
            products.append((0, cheapest[1]))
            return products
        else:
            return super().summary()


if __name__ == "__main__":
    c = Above3ProductsCheapestFreeCart()
    c.add(10, "a")
    c.add(20, "b")
    c.add(4, "c")
    c.add(3, "d")
    print(c.summary())
