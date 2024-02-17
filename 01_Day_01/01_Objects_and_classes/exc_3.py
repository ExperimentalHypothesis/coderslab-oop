
class BankAccount:
    def __init__(self, number: int):
        self.number = number
        self.cash = 0

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Cant deposit negative amount")
        self.cash += amount

    def withdraw(self, amount: float):
        if amount > self.cash:
            disposable = self.cash
            self.cash = 0
            return disposable

        self.cash -= amount
        print("else")
        return amount

    def print_info(self):
        print(f"Bank account nr {self.number} has cash {self.cash}")


if __name__ == "__main__":
    ba = BankAccount(1)
    ba.deposit(300)

    withdrawn = ba.withdraw(200)
    print(withdrawn)  # 200
    ba.print_info()

    withdrawn = ba.withdraw(200)
    print(withdrawn)  # 100
    ba.print_info()

    withdrawn = ba.withdraw(200)
    print(withdrawn)  # 0
    ba.print_info()

