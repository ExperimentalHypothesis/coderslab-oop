![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Exercise 1

Using the module `re`, write a function named `check_dice` which accepts a single parameter in the form of a string.
The function should check if there is a valid dice throw pattern in the passed parameter.

The dice roll pattern has the following form:

```plaintext
<number of rolls>d/D<number of die sides>+/-<result modifier>
```

e.g.

`2d10+20` - two rolls of a 10-sided die, add 20 to the result

`6D3-10`- six rolls of a 3-sided die, subtract 10 from the result

`D6` - one roll of a 6-sided die

The function should return `True` if there is a valid formula in the passed parameter, otherwise the function should return `False`.

Examples of how the function works:

`check_dice("8d7+10")` - returns `True`

`check_dice("8s7+10")` - returns `False`

`check_dice("8D7+10 abcdefghijk")` - returns `True`

`check_dice("8d-h")` - returns `False`


## Exercise 2

Open the file `exercise_2.py`. There is variable `text_to_search` in it, which contains Act I of The Tragedy of Macbeth by William Shakespeare
(text retrieved from [http://shakespeare.mit.edu/](http://shakespeare.mit.edu/macbeth/full.html)).

Using the module `re` perform the following tasks:

1. find all occurrences of the word `love`.
2. find all occurrences that match the pattern `<sure>%`.
3. find all occurrences of words that end with the character `?`.
4. find all words that contain the string `fair` (regardless of character case).
