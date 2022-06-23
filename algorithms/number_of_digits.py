"""
Write a Python function that accepts "a number" and outputs the number of (base-10)
digits needed to write the integer part of that number on a piece of paper. Here,
"a number" is any Python type in the standard library that behaves as a number
(including but not limited to `int` and `float`).

Example input & output

(in=100, out=3), (in=999, out=3), (in=-10, out=2), (in=3.1415, out=1)

Our evaluation checklist

✅ Correct output for all `int`s and `float`s (including edge cases)

✅ Correct output for the other number types in Python's standard library

✅ Tests that convince us that your implementation is correct

✅ Correct & complete type annotations for the input and output

✅ At most 50 lines of code (including comments, excluding imports, excluding tests)

✅ Function docstring that follows any convention (NumPy, Google, ...)

✅ In-line comments that explain the purpose of lines that are not self-explanatory

✅ The implementation "reads like a book"

⚠️ We will not evaluate the speed of your program in any way, shape, or form!
"""
import math
from decimal import Decimal
from fractions import Fraction
from typing import Union


def number_of_digits(number: Union[int, float, complex, bool, Fraction, Decimal]) -> int:
    """
    :param number: any Python type in the standard library that behaves as a number
    :return: The number of (base-10) digits needed to write the integer part of that number on a piece of paper
    """
    if number == math.inf:
        return 0  # Infinite is represented with the symbol "∞", which is not a digit
    if type(number) == complex:
        return 0  # Complex (imaginary) numbers are represented with the letter "i", which is not a digit
    if number < 0 or number in [True, False]:
        number = abs(number)
    if type(number) == Fraction:
        number = float(number)
    if type(number) in [float, Decimal]:
        integer_part = int(str(number).split(".")[0])
        number = integer_part

    number_of_integer_digits = len(str(number))

    return number_of_integer_digits
