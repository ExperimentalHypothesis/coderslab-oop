![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Exercise 1

### Part 1

Write a class named `Product` that takes the arguments `name`, `price` in the method `__init__` and stores them as product attributes.

Additionally, `__init__` should set the unique attribute `id` in the product.

### Part 2

Write a class named `ShoppingCart`. Its `__init__` method requires no attributes (except, of course, `self`).

The `__init__` method should create in the shopping cart instance:
 - an empty dictionary named `products` (as an attribute). The key in this dictionary will be product's `id`, and the value will be whole products (instances of the `Product` class).
 - an empty dictionary named `quantities` (as an attribute). The key will be the product's `id`, and the value will be the number of pieces of that product in the cart.

The class should also have the following methods:

 - `add_product(product)` - this method should add a new product to the `products` dictionary and update the quantity of this product in the `quantities` dictionary.
 - `remove_product(product)` - this method should remove the product from the cart (consider both dictionaries: `products` i `quantities`). If such a product has not been scanned before, it is supposed to do nothing.
 - `change_product_quantity(product, new_quantity)` - this method should change the quantity of a given product in the cart. If such a product has not been scanned before, it should do nothing. If `new_quantity` is zero, remove the product from the cart. Passing a negative `new_quantity` should throw an exception `ValueError` with an appropriate comment.
 - `get_receipt()` - this method should create a receipt. It should not print on its own (use `print(...)`), instead it should return a string. An example of the expected receipt can be found at the end of the exercise.

All the above arguments named `product` should be instances of the `Product` class.

### Part 3

Modify the `get_receipt()` method to give a 30% discount on the total price for a product if there are at least 3 items of that product in the cart.

### Usage example:

```python
>>> bread = Product('Bread', 2.70)
>>> ham = Product('Ham', 8.40)
>>> cheese = Product('Cheese', 4.40)
>>> chive = Product('Chives', 1.50)
>>> pepper = Product('Pepper', 2.35)

>>> print(bread.id)
1
>>> print(pepper.id)
5
>>> print(pepper.name)
'Pepper'
>>> print(pepper.price)
2.35

>>> cart = ShoppingCart()
>>> print(cart.products)
{}
>>> print(cart.quantities)
{}
>>> print(cart.get_receipt())
Total: 0 EUR

>>> cart.add_product(bread)
>>> cart.add_product(bread)
>>> cart.add_product(bread)
>>> cart.add_product(pepper)
>>> cart.add_product(chives)
>>> cart.change_product_quantity(pepper, 2)
>>> print(cart.products)
{1: <...Product object...>, 5: <...Product object...>, 4: <...Product object...>}
>>> print(cart.quantities)
{1: 3, 5: 2, 4: 1}

>>> cart.remove_product(bread)
>>> print(cart.get_receipt())
# The order of products may vary
Pepper - quantity: 2, price: 2.35 EUR, total: 4.7 EUR
Chives - quantity: 1, price: 1.5 EUR, total: 1.5 EUR

Total: 6.2 EUR
```


ï»¿# Exercise 2

Write a `Price23Vat` class. Its `__init__` method should take value: the pretax amount, and store it as a  `_pretax` attribute.

Apart from this, based on the pretax amount `__init__` should calculate the  `_net` and `_tax` attributes. Take 23% VAT as suggested by the name of the class.

Add methods: `get_net()`, `get_pretax()` and `get_tax()` returning the amounts of their respective attributes.

Add methods: `set_net(value)`, `set_pretax(value)` and `set_tax(value)` storing the passed argument and calculating and storing the remaining two.


ï»¿# Exercise 3

To the `Square` class we have written together, add the getters and setters for the side area, perimeter and diagonal, using `@property`.

Getters may return the values of attributes or the result of the calculation of their respective `get_...` methods.

Setters should use the existing `set_...` methods to avoid duplicating code.

Example:
```python
square = Square(11)

print(square.get_side())  # 11
print(square.side)        # 11
print(square.perimeter)   # 44

square.perimeter = 48

print(square.get_side())  # 12
print(square.side)        # 12
print(square.perimeter)   # 48
```


ï»¿# Exercise 4

Write the `Price23Vat` class again but **this time use `@property`** to create getters and setters for: pretax, net and tax amounts. Do not write the `get_...` and `set_...` methods.

Example:
```python
price = Price23Vat(123)

print(price.pretax)        # 123
print(price.tax)           # 23
print(price.net)           # 100

price.tax = 69

print(price.pretax)        # 369
print(price.tax)           # 69
print(price.net)           # 300
```
