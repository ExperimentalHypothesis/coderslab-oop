class Calculator:
    def __init__(self):
        self.operations = []

    def add(self, a, b):
        res = a + b
        self.operations.append(f"added {a} to {b} got result {res}")
        return res

    def multiply(self, a, b):
        res = a * b
        self.operations.append(f"multiplied {a} by {b} got result {res}")
        return res

    def print_operations(self):
        for i in self.operations:
            print(i)




if __name__ == "__main__":
    c = Calculator()
    c.add(1,2)
    c.multiply(10,20)
    c.print_operations()
