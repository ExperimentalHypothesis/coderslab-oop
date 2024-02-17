class Price:
    EUR_PLN_RATE = 4.5
    USD_PLN_RATE = 3.8

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def from_eur(cls, amount: float):
        return cls(
            amount * cls.EUR_PLN_RATE)  # misto cls.EUR_PLN_RATE muze byt Price.EUR_PLN_RATE ale bude v tom rozdil pri dedeni

    @classmethod
    def from_usd(cls, amount: float):
        return cls(amount * cls.USD_PLN_RATE)

    def __str__(self):
        return f"{self.value} PLN"


if __name__ == "__main__":
    a = Price(10)
    print(a)

    some_price = Price.from_usd(25)
    print(some_price)

    some_other_price = Price.from_eur(80)
    print(some_other_price)
