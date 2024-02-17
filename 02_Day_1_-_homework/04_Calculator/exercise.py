class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


class LoggingCalculator(Calculator):
    def __init__(self):
        self.history = []

    # Ted tady udelam celkem silenost - dekotorovou faktory, co dovoli prepouzit ten log na jakoukoliv metodu
    # Moc se mi to nelibi ale je to jen ukazka toho, co je mozne.. Misto rcniho psani printu do kazde metody
    @staticmethod
    def log(operator):
        def decorator(foo):
            def wrapper(self, a, b):
                result = foo(self, a, b)
                self.history.append(f"{a} {operator} {b} = {result}")
                return result
            return wrapper
        return decorator


    # Ted tady kazdou metodu muzu ted jednoduse "odekorovat"
    @log("+")
    def add(self, a, b):
        return super().add(a, b)

    @log("-")
    def sub(self, a, b):
        return super().sub(a, b)

    @log("*")
    def mul(self, a, b):
        return super().mul(a, b)

    @log("/")
    def div(self, a, b):
        return super().div(a, b)


if __name__ == "__main__":
    calc = LoggingCalculator()
    print(calc.add(2, 3))
    print(calc.mul(3, 3))
    print(calc.sub(7, 4))
    print(calc.div(5, 2))
    print(calc.history)
