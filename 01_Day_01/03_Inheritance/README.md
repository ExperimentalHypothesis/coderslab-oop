![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


### Class `Cart`

Create a `Cart` class - it will represent the shopping cart in an online store.

In the `__init__` method create an attribute named `products` - it should be an empty list at the beginning.

Create an `add` method that takes two arguments: price (of the `int` or `float` type) and product name (of the `str` type). The method should append a tuple `(name, price)` at the end of the list in the `products` attribute.

Create a `summary` method that simply returns the value of the `products` attribute.

### Class `Discount20PercentCart`

Write a `Discount20PercentCart` class that inherits from the `Cart` class.

The `summary` method of the `Discount20PercentCart` class should return a list of tuples (similar to `summary` in the `Cart` class), but the prices are to be reduced by 20%.

### Class `Above3ProductsCheapestFreeCart`

Write an `Above3ProductsCheapestFreeCart` class that inherits from `Cart`.

The `summary` method of the `Above3ProductsCheapestFreeCart` class should return a list of tuples; if there are more than 3 products in the list, the price of the cheapest one should be changed to zero.

**Tests are attached to the task - you can run them using the command `python3 -m unittest`**.
