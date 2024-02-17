class Employee:
    def __init__(self, id_, first_name, last_name):
        self.id_ = id_
        self.first_name = first_name
        self.last_name = last_name
        self._salary = 0

    def set_salary(self, salary: float | int):
        if not isinstance(salary, float | int):
            raise TypeError("Salary must be numerical")
        if salary < 0:
            raise ValueError("Salary must be positive")

        self._salary = salary


if __name__ == "__main__":
    e = Employee(1, "john", "lennon")
    try:
        e.set_salary(-1)
        e.set_salary("xxx")
        e.set_salary(1000.0)
    except TypeError as er:
        print(er)
    except ValueError as er:
        print(er)


