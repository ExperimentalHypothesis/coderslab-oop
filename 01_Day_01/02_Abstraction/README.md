![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


ï»¿# Exercise 1

In `exercise.py` there's an application that simulates stock exchange trading.

In a loop the application shows your wallet balance (Polish zloty and US dollars), as well as the PLN/USD exchange rate, and asks for your decision. Possible decisions are:
- `buy` - use all of your PLN to buy USD
- `sell` - sell all of your USD
- `wait` or **empty string** - do nothing: wait for the exchange rate to change

The code passes all automatic tests but it is written in a very messy way. You need to select its fragments (sub-exercises) and write the classes to solve each of them in full; replace the original code with your classes. Once your refactoring is done the tests should still pass.

Note that the tests require the `exercise.py` to have the `main(usdpln_rates)` function and to use `input(...)` and `print(...)` to communicate with the user. All messages need to remain unchanged.

## Class to write: `CommandPrompt`

Write a class to handle asking for the user's decision.

The `__init__` method should take three arguments:
- a list/tuple of strings appropriate for the **buy** command
- a list/tuple of strings appropriate for the **sell** command
- a list/tuple of strings appropriate for the **wait** command

The `ask(self)` method should prompt the user to decide and return only one of the three strings: `"buy"`, `"sell"` or `"wait"`. If the user input is anything not included in the lists passed to `__init__`, it should display a message `Invalid choice: <SHOW USER INPUT HERE>` and ask again.

Create an instance of this class **above the function** `main(usdpln_rates)`, and use its `ask()` method in the function. When you create the instance, give the same data (tuples of strings), so that the program works the same as before your changes.

## Class to write: `Wallet`

Write a class to handle storing currencies.

The `__init__` method should take 2 arguments: the initial amount of zlotys and the initial amount of dollars. Before you store the two values in the instance make sure their type is `float`.

Write the `convert_pln_to_usd(self, usdpln_rate)` and`convert_usd_to_pln(self, usdpln_rate)` methods. Each of them should take all available zlotys or dollars and, using the given exchange rate, convert them to dollars and zÅotys respectively.

Create the instance of this class **at the beginning of the function** `main(usdpln_rates)`, and in the function use its methods and attributes. When you create the instance, give it the data (initial amounts of zlotys and dollars), so the program works the same as before the changes.


ï»¿# Exercise 2

## `middle_elements` function

In `exercise.py` write the `middle_elements(sequences)` function, that from any sequence (list, tuple, etc.) listed in `sequences` will take the middle element and return a list composed only of the middle elements.

Use `len(...)` to check the length of each sequence and evaluate the index of its middle element; use square brackets to pick the element.

Use the `python -m unittest` command (or `python3 -m unittest`) to run automatic tests for this exercise.

If any of the sequences has an even number of elements, pick the one on the right from the middle pair. If any of the sequences is empty - skip it.

Example:

```python
>>> print(middle_elements(
...  [
...    [6, 7, 8, 9, 10],  # middle element is 8
...    ["Who", "is", "that?"],  # middle element is "is"
...    [],  # empty - skip it
...
...    # middle elements are: "seven" and "eight" - pick "eight"
...    ["six", "seven", "eight", "nine"],
...  ]
...))
[8, "is", "eight"]
```

## Class `SequenceOfNumbers`

Next, write the `SequenceOfNumbers` class. This class will be able to represent a sequence of numbers of any length with just 3 numbers necessary to define the sequence.

Let its `__init__` method take three arguments: `start`, `stop` and `step`. The class is supposed to represent the sequence of numbers from `start` to `stop` (excluding `stop`), with the distance of `step` between the numbers.

Example: `SequenceOfNumbers(14, 46, 4)` will represent the following sequence:

```bash
Indexes:    0       1       2       3       4       5       6      7
Elements:  14      18      22      26      30      34      38      42   # 46
           ^start                       stop is not a part of the sequence^

Length: 8
```

## Magic method `__len__`

Add a `__len__` method to the class that will use `start`, `stop` and `step` to calculate the length of the sequence.

Thanks to this method Python's built-in `len()` function will know how to communicate with the`SequenceOfNumbers` class.

```python
>>> nums = SequenceOfNumbers(14, 46, 4)
>>> len(nums)
8
```

## Magic method `__getitem__`

Add a `__getitem__` method to the class that (apart from `self`) will take the `index` argument, and will return the number at the `index` of the sequence.
If the `index` given by the user is too big or negative, throw an `IndexError` exception with an appropriate message.

This method is needed to query `SequenceOfNumbers` for its elements as if it was a list or tuple: using square brackets.

```python
>>> nums = SequenceOfNumbers(14, 46, 4)
>>> nums[0]
14

>>> nums[7]
42

>>> nums[2]
22

>>> nums[-1]
Traceback (most recent call last):
...
IndexError: 'Negative indexes are not supported, sorry!'

>>> nums[8]
Traceback (most recent call last):
...
IndexError: 'Always look beyond the horizon, but never beyond the end of sequence!'
```

## SequenceOfNumbers now has the interface required by `middle_elements`

Use the `middle_elements` function, and (as its argument) pass a list of lists, tuples and the `SequenceOfNumbers` objects. If everything works out as planned, `middle_elements` will take the middle number from the `SequenceOfNumbers` object.

### Hint:
For **b** - beginning, **e** - end, **d** - difference, **ceil(...)** - rounding up:

Length of sequence: `ceil((e - b) / d)`

n-th element: `b + n * d`


ï»¿# Exercise 3

In `app.py` you'll find a script that helps to manage a small bookshop. It handles stock updates, downloading information from Google Books about new books in stock, and printing stickers with price and barcode.

Example of use:
```bash
# add book based on ISBN, with the price of 12.50
python app.py import 9781573561075 12.50

 # add 7 books to stock
python app.py add 9781573561075 7

 # remove 2 books from stock
python app.py remove 9781573561075 2

# print a sticker with price and barcode
python app.py print-price-sticker 9781573561075
```

Your task it to clean up the code:
- divide the exercise ("problem") to smaller ones
- pick one of them
- write a class to solve one of the problems in full; best do it in a separate file
- remove the earlier code handling the problem: replace it using your class
- repeat the steps until the code is clean, readable and easy to understand

Hint: fragments that should have their own classes include:
- querying Google Books for book details
- handling stock, with methods for:
  - storing book information
  - adding a number of items of a book to stock
  - removing a number of items of a book from stock
  - reading information about a book
- generating a price sticker

**Additionally** you can use a  [parser](https://docs.python.org/3/library/argparse.html) to read the data you need.


ï»¿# Exercise 4

In this exercise you will create a questionnaire. You'll write a `Questionnaire` class that will collect all questions, and a `SingleChoiceQuestion` that will handle displaying a specific question and collecting user's response.

If you want, try to add more classes of questions, e.g,. multiple choice questions or open questions.

## Class `SingleChoiceQuestion`

Write the `SingleChoiceQuestion` class. Its `__init__` method should take: two arguments:
- question text (string type)
- list of answers (list/tuple of strings)

Write an `ask(self)` method that:
- displays a question
- displays answers: one per line, preceded by consecutive letters: as shown in the example at the end of the exercise
- prompts user to give the answer (only the letters assigned to available options are allowed: for a question with the choice of three options, valid choices are `"a"`, `"b"` or `"c"`)
- displays an empty line
- returns the answer

## Class `Questionnaire`

Write a `Questionnaire` class. Its `__init__` method should take one argument: title.

Add an `add_question(self, question)` method that will add a question (that is: an object of `SingleChoiceQuestion` class) to the list of questions. In the `__init__` method make sure that every instance of the `Questionnaire` class has such a list: initially empty.

Add a `run()` method that:
- displays the questionnaire title and a single empty line,
- for each question (object of the`SingleChoiceQuestion` class) starts its  `ask()` method,
- displays string `'Thank you!'`
- returns a dictionary with numbers of questions (starting from zero) as keys, and as values: the results of `ask()` called on question objects.

## Expected result:

```python
>>> questionnaire = Questionnaire('Laptop satisfaction questionnaire')
>>> q1 = SingleChoiceQuestion('Size of screen', ['less than 15 inches', 'from 15 to 17 inches', 'more than 17 inches'])
>>> q2 = SingleChoiceQuestion('Type of screen', ['matte', 'glossy'])
>>> q3 = SingleChoiceQuestion('Would you recommend it?', ['definitely yes', 'rather yes', 'not sure', 'rather not', 'definitely not'])
>>> questionnaire.add_question(q1)
>>> questionnaire.add_question(q2)
>>> questionnaire.add_question(q3)
>>> answers = questionnaire.run()
Laptop satisfaction questionnaire

Size of screen
a) less than 15 inches
b) from 15 to 17 inches
c) more than 17 inches
Answer: c  # script waits for the user's answer here. We answer with "c"

Type of screen
a) matte
b) glossy
Answer: c # script waits here. We answer with (invalid) "c"
Invalid answer, try again: a # now we pick a valid choice: "a"

Would you recommend it?
a) definitely yes
b) rather yes
c) not sure
d) rather not
e) definitely not
Answer: b # script waits here. We answer with "b"

Thank you!
>>> print(answers)
{0: 'c', 1: 'a', 2: 'b'}
```

Hint:

`chr(97)` is `"a"`, `chr(98)` is `"b"`, `chr(99)` is `"c"`...

`ord("a")` is `97`, `ord("b")` is `98`, `ord("c")` is `99`...
