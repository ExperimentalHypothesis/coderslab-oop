![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Exercise 1 &ndash; done with the lecturer

Create a class named `Calculator`. The constructor should take no data.
Each newly created object should have an empty list, in which it will keep the history of called operations (create it in the constructor).
Then add the following methods to the class:

1. `add(num1, num2)` &ndash; method has to add two variables and return the result. Additionally, in the list of operations it is supposed to store the statement: "added `num1` to `num2` got `result`".
2. `multiply(num1, num2)` &ndash; method has to multiply two variables and return the result. Additionally, in the list of operations it is supposed to store the statement: "multiplied `num1` by `num2` got `result`".
5. `print_operations()` &ndash; method has to print out all stored operations.

Remember to use `self` in appropriate places.
Create some calculators and test them.


## Exercise 2

Create a `Shape` class with the following requirements:

1. It has attributes:
`x`, `y` (specifying the center of this shape) and `color`;
2. has a `describe` method, outputting information about this shape;
3. has a `distance` method, returning the distance from centers of this and another shape.
The method should take as a parameter another object of the `Shape` class and count the distance from the centers of both shapes
(how? recall Pythagoras' theorem);
4. has the `__str__` method overwritten so that when the object is projected to a string, the program returns:
"Figure of the *color* color with center at point (*x*, *y*)".


## Exercise 3

Create a `BankAccount` class that will satisfy the following requirements:

1. Have the attributes:
 * `number` - this attribute should store the account ID number (for the sake of simplicity, you can assume that the account number can be any integer);
 * `cash` - an attribute specifying the amount of money in the account. This must be a floating point number.
2. Have a constructor that accepts only the account number. The attribute `cash` should always be set to 0.0 for a newly created account.
3. Have a `deposit_cash(amount)` method whose role is to increment the value of the `cash` attribute by the specified value.
Remember to check if the given value is greater than 0.0.
4. Have a `withdraw_cash(amount)` method whose role is to decrease the value of the `cash` attribute by the given value.
The method should return the amount of money paid out. For the sake of simplicity, assume that the amount of money in the account cannot go below 0.0, e.g. if you try to withdraw 500 EUR from an account that has only 300 EUR, the method will return 300 EUR. Remember to check if the given value is greater than 0.0.
5. Have a `print_info()` method that does not take any parameters.
This method should display information about the account number and its status.


## Exercise 4

Create an `Employee` class that will satisfy the following requirements:

1. Have the following attributes:
 * `id` - this attribute should store the employee ID number,
 * `first_name` - attribute that specifies the employee's first name,
 * `last_name` - attribute that specifies the employee's last name,
 * `_salary` - attribute that specifies how much the employee earns per hour. Note the underscore which states that this attribute should not be accessible outside the class.
2. Have a constructor that takes id, first name, and last name.
3. Have a `set_salary(salary)` method that sets the value of the `salary` attribute.
Remember to check that the specified value is:
 * A numeric value,
 * Greater than (or equal to) 0.0.

#### Hint: if you want to check the type of a variable, use the function `isinstance()`: [https://docs.python.org/3/library/functions.html#isinstance](https://docs.python.org/3/library/functions.html#isinstance)
