![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


﻿# Exercise 1

Your task is to write a set of classes modeling food ingredients, meals, and a daily plan. They will make it possible to easily count how much protein, carbohydrates, fats and calories are provided in each plan.

## Ingredient

Write a class representing an ingredient of a meal. Its `__init__` method should take:
- name (`str`)
- amount of protein in 100g of product (`float` or `int`)
- amount of carbohydrates in 100g of product (`float` or `int`)
- amount of fats in 100g of product (`float` or `int`)

## Meal

Write a class representing meals. Its `__init__` method should take one argument: the name of a meal.

Write a method for it that will enable adding a specific amount of ingredients (in grams).

## Daily plan

Write a class representing a daily plan. It should have a method to add new meals and another method printing the summary (see example below)

```
# Watch out, this is pseudocode!

egg = Create Ingredient Egg: protein = 13, carbohydrates = 1.1, fats = 11
tomato = Create Ingredient Tomato: protein = 0.9, carbohydrates = 3.9, fats = 0.2
bread = Create Ingredient Bread: protein = 9, carbohydrates = 49, fats = 3.2

scrambled_eggs = Create Meal Scrambled Eggs
add 200g egg to scrambled_eggs
add 50g tomato to scrambled_eggs

sandwich = Create Meal Sandwich
add 25g bread to sandwich
add 50g tomato to sandwich

very_minimalistic_menu = Create Minimal Plan
add scrambled_eggs to very_minimalistic_menu
add sandwich to very_minimalistic_menu

show summary very_minimalistic_menu
```
Output (summary of "Minimal" plan):
```
Minimal

Meal: Scrambled Eggs
- 200g Egg (26g protein, 2.2g carbohydrates, 22g fats, 310.8 kcal)
- 50g Tomato (0.45g protein, 1.95g carbohydrates, 0.1g fats, 10.5 kcal)
Total: 26.45g protein, 4.15g carbohydrates, 22.1g fats, 321.3 kcal

Meal: Sandwich
- 25g Bread (2.25g protein, 12.25g carbohydrates, 0.8g fats, 65.2 kcal)
- 50g Tomato (0.45g protein, 1.95g carbohydrates, 0.1g fats, 10.5 kcal)
Total: 2.7g protein, 14.2g carbohydrates, 0.9g fats, 75.7 kcal

TOTAL: 29.15g protein, 18.35g carbohydrates, 23g fats, 397 kcal
```

## Calories

Ingredient calories are calculated with the formula:
```
kcal = protein * 4 + carbohydrates * 4 + fats * 9.4
```


﻿# Exercise 2

Write a `Price` class, whose `__init__` method takes a number (`int` or `float`) - price in Polish złoty (PLN). Store the given number as an attribute of `value` and make sure its type is `float`; even if `__init__` gets passed an `int` number. Also make sure that the amount has at most 2 decimal places.

Add alternative methods of creating the `Price` object based on amounts in euro and US Dollars:

```python
some_price = Price.from_usd(25)
some_other_price = Price.from_eur(80)
```

Use the exchange rates: **EURPLN = 4.5 PLN** oraz **USDPLN = 3.8 PLN**.

Add an `__str__` method taking one argument (`self`) and returning a string: amount text followed by `PLN` (add a space between the amount and `PLN`).

```python
>>> print(some_price)
95.0 PLN
>>> print(some_other_price)
360.0 PLN
```


﻿# Exercise 3

In this exercise you will write a `Student` class representing a primary school student.

Information about them we want to store is:
- name
- surname
- class (e.g., group `'1A'` or `'5B'`)
- year of birth
- average of grades

Such information, in this order will be passed while creating an instance of the `Student` class.

Additionally there should be a way to create multiple instances of the `Student` class based on a list of students in a `.csv` file. This way should allow us to optionally filter the students based on the group they're in, e.g., to only select the students from `'1A'` group.

# Solution

Let's start by writing a simple class with an `__init__` method:

```python
class Student:
    def __init__(self, name, surname, school_class, year_of_birth, grade_avg):
        self.name = name
        self.surname = surname
        self.school_class = school_class
        self.year_of_birth = year_of_birth
        self.grade_avg = grade_avg
```

Now we can create an instance of the `Student` class:

```python
john = Student('John', 'Smith', '1A', 2012, 4.78)
jane = Student('Jane', 'Adams', '2C', 2011, 5.11)
```

Before we write a method to read the students from a file, let's talk about opening files and taking the information from CSV files in particular. 

## Reading text files

### Opening

Python has an `open(...)` function that returns an object representing a file; from this object, using its methods we can get its content in a variety of ways.

The most important arguments of the `open` function:
- `file` - path to the file (if the file and script are in the same folder, the filename is enough),
- `mode` - what type of file we're opening and why. **default value is `'r'`** it means that we're opening a text file in read-only mode. About all the options you can read [here: `open` function in Python documentation](https://docs.python.org/3/library/functions.html#open).

```python
my_file = open('my_file.txt')
```

### Reading

Now the `my_file` variable stores the object representing the file from the hard drive. We can read its data in a few ways:
- `my_file.read()` - returns the entire content of the file as a string,
- `my_file.readline()` - returns a single line as a string (it "remembers" what has already been read - next time the method is called, the next line will be returned),
- `my_file.readlines()` - returns all lines as a list of strings,

There's one more way of reading lines from a file: iterating through the object:

```python
for line in my_file:
    print('A line from the file:', line)
```

### Closing

Once you finish working with a file you should close it:

```python
my_file.close()
```

But there is a better way, you can use the object with a file as a **context manager**. Thanks to this the file will close as soon as the block of code that uses it ends:

```python
with open('my_other_file.txt') as my_other_file:
    print('Is the file closed?', my_other_file.closed)
    data = my_other_file.readline()
    print('Again, is the file closed?', my_other_file.closed)
print('How about now?', my_other_file.closed)  # Notice: no indent unlike in the lines above
```

The result is:
```
Is the file closed? False
Again, is the file closed? False
How about now? True
```

## Reading CSV files

### file structure

CSV is short for Comma Separated Values: this alone tells a lot about how the data in the file is organized. CSV files are used to store tabular data: a line in a file is a row in a table with each cell in one row delimited with commas.

Example:

```
1,Fruit of the Loom Girls Socks,7.97,0.60,8.57
2,Rawlings Little League Baseball,2.97,0.22,3.19
3,Secret Antiperspirant,1.29,0.10,1.39
4,Deadpool DVD,14.96,1.12,16.08
5,Maxwell House Coffee 28 oz,7.28,0.55,7.83
6,Banana Boat Sunscreen 8 oz,6.68,0.50,7.18
7,Wrench Set 18 pieces,10.00,0.75,10.75
8,M and M 42 oz,8.98,0.67,9.65
9,Bertoli Alfredo Sauce,2.12,0.16,2.28
10,Large Paperclips 10 boxes,6.19,0.46,6.65
```

### Reading

Fortunately, Python's standard library has a `csv` module with a `reader` function. This function takes an open csv file as an argument and returns an object that allows to read the data from the file easily:

```python
import csv

with open('my_file.csv') as my_file:
    my_reader = csv.reader(my_file)
```

We can iterate over the object created this way with a `for` loop: individual values will be lists of strings and each string will correspond to one cell in a row.

```python
import csv

with open('my_file.csv') as my_file:
    my_reader = csv.reader(my_file)
    for row in my_reader:
        print(f'Name: {row[1]}; Price: {row[4]}')
```

The result is:
```
Name: Fruit of the Loom Girls Socks; Price: 8.57
Name: Rawlings Little League Baseball; Price: 3.19
Name: Secret Antiperspirant; Price: 1.39
Name: Deadpool DVD; Price: 16.08
```

## The method reading students from a file

We already know how to get data from a csv file so we can start writing the method. Let's call it `from_file`; at the beginning it will only require giving the name of a file. Within this method we are going to create multiple **wiele** instancji klasy `Student` - przyda się nam zatem lista, w której zapamiętamy te instancje, i którą zwrócimy gdy będzie kompletna.

```python
import csv

class Student:
    def __init__(self, name, surname, school_class, year_of_birth, grade_avg):
        self.name = name
        self.surname = surname
        self.school_class = school_class
        self.year_of_birth = year_of_birth
        self.grade_avg = grade_avg

    @classmethod
    def from_file(cls, file):
        students = []
        with open(file) as students_file:
            for row in csv.reader(students_file):
                students.append(
                    cls(row[0], row[1], row[2], int(row[3]), float(row[4]))
                )
        return students
```

A method written like this will be able to read the data from a file:
```
John,Smith,1A,2012,4.78
Jane,Adams,2C,2011,5.11
Mike,Brown,2C,2011,5.08
```

## Filtering students by class

The final functionality required in the instruction is filtering students by class when reading from the file. That's why the `from_file` method is going to get an additional argument: `class_name`, with a default value of `None` meaning that filtering is turned off. We can't use the word `class` as a name of the argument because it is a reserved keyword in Python.

```python
    ...

    @classmethod
    def from_file(cls, file, class_name=None):
        students = []
        with open(file) as students_file:
            for row in csv.reader(students_file):
                students.append(
                    cls(row[0], row[1], row[2], int(row[3]), float(row[4]))
                )
        return students
```

Now the method takes the additional argument so we can use it in two ways:

```python
Student.from_file('students.csv')  # ALL students
Student.from_file('students.csv', '2A')  # Only those in 2A class
```

Let's make sure that the `from_file` method considers the given class designation.

The class designation is in the third column of the csv file: that is, at index 2 (we count from 0), in the `row` variable. We need to ensure that students get added to the `students` list only if: `class_name` has a value of `None` **or** `class_name` is the same as `row[2]`:

```python
    ...

    @classmethod
    def from_file(cls, file, class_name=None):
        students = []
        with open(file) as students_file:
            for row in csv.reader(students_file):
                if class_name is None or class_name == row[2]:
                    students.append(
                        cls(row[0], row[1], row[2], int(row[3]), float(row[4]))
                    )
        return students
```

# Summary

The example above shows that the methods with `@classmethod` decorator are not limited to creating only one instance based on the data other than expected by the `__init__` method. In this case the method returned a list of multiple instances and the data needed to create them was not passed by arguments: they were all read from a file! Python does not, in any way, limit what the methods with `@classmethod` decorator can return. Python gives us the tools and we can decide what to do with them.


﻿# Exercise 4

Write a `Calculator` class with the following methods:
- `add(a, b)` - returns result of addition,
- `sub(a, b)` - returns result of subtraction,
- `mul(a, b)` - returns result of multiplication,
- `div(a, b)` - returns result of division,

Write a `LoggingCalculator` class inheriting from `Calculator`.

The `LoggingCalculator` class should create a `history` attribute with an empty list as the initial value.

To the `LoggingCalculator` class add the `add`, `sub`, `mul` and `div`methods that with `super()` will use their counterparts from the `Calculator` class, and will add a string with the record of the performed mathematical operation at the end of the list in the `history` attribute, and only then return the result.

Example:

```python
calc = LoggingCalculator()
print(calc.add(2, 3))
print(calc.mul(3, 3))
print(calc.sub(7, 4))
print(calc.div(5, 2))
print(calc.history)
```

Result

```
5
9
3
['2 + 3 = 5', '3 * 3 = 9', '7 - 4 = 3', '5 / 2 = 2.5']
```

**There are tests attached to the exercise; you can run them using the `python3 -m unittest` command.**


﻿# Exercise 5

Write a `Book` class with an `__init__` method that takes three arguments: `title`, `author` and `isbn`, and stores them in the instance as attributes with the same names.

Add a `check_isbn` method that takes a single argument: ISBN number (as a string), validates it and returns `True` or `False`. It should be possible to use the method even without an instance of the `Book` class; use a `@staticmethod` decorator.

Add code to the `__init__` method that will  use the `check_isbn` method and throw a `ValueError` exception in case of creating a book (instance of `Book` class) with invalid ISBN number.

[ISBN number validation rules](https://isbn-information.com/check-digit-for-the-13-digit-isbn.html) - program validating 10 and 13-digit ISBNs, and allow passing ISBNs with separators (i.e., `0-306-40615-2`) and without (i.e., `0306406152`). You may also want to check [ISBN Wikipedia entry](https://en.wikipedia.org/wiki/ISBN).
