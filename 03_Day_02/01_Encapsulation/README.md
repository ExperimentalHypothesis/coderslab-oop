![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


Create a `Square` class. Let its `__init__` method take one argument: length of side, and store it as the `_side` attribute. Note the `_` character starting the attribute name!

Features of squares include:
- length of side
- perimeter
- area
- diagonal

Develop the `__init__` method: based on the given length of side, let it **calculate** the perimeter, area and diagonal, and store these numbers as `_perimeter`, `_area` and `_diagonal`.

Add the `get_side()`, `get_perimeter()`, `get_area()` and `get_diagonal()` methods that will simply return the values of the attributes they correspond to.

Is should be possible to change the size of the square in a few ways:
- by specifying the new length of the size,
- by specifying the new perimeter,
- by specifying the new area,
- by specifying the new diagonal.

Write methods: `set_side(new_length)`, `set_perimeter(new_length)`, `set_area(new_area)` and `set_diagonal(new_length)`. Each of them should store the argument in its corresponding attribute and update the remaining attribute so that the `Square` instance has coherent data.

## For volunteers

There are automated tests for creating the instance, reading and storing side length, area and diagonal. Look at these tests and in a similar way create the tests:
- `test_reading_perimeter` for the method of reading the perimeter (based on the other `test_reading_...` tests)
- `test_setting_perimeter` for the method of editing the square based on perimeter
- Modify the tests: `test_setting_area`, `test_setting_diagonal` and `test_setting_side` so that they also check the perimeter.

If your calculation results have decimal values, use `assertAlmostEqual` instead of `assertEqual` - computers don't always handle such numbers correctly: check what the result of `0.1 + 0.1 + 0.1` is.
