import math
from decimal import Decimal
from fractions import Fraction

import pytest

from algorithms.number_of_digits import number_of_digits


class TestNumberToDigits:
    @pytest.mark.parametrize("number, result", [
        (100, 3),
        (999, 3),
        (-10, 2),
        (0, 1),
    ])
    def test_handles_integers(self, number, result):

        assert number_of_digits(number) == result

    @pytest.mark.parametrize("number, result", [
        (-10.1, 2),
        (3.1415, 1),
    ])
    def test_handles_floats(self, number, result):

        assert number_of_digits(number) == result

    @pytest.mark.parametrize("number, result", [
        (Decimal("7.9"), 1),
        (Decimal("-3.1"), 1),
    ])
    def test_handles_decimals(self, number, result):

        assert number_of_digits(number) == result

    @pytest.mark.parametrize("number, result", [
        (Fraction(1, 2), 1),
        (Fraction(42567, 2734), 2),
        (Fraction(-2, 3), 1),
    ])
    def test_handles_fractions(self, number, result):

        assert number_of_digits(number) == result

    @pytest.mark.parametrize("number, result", [
        (True, 1),
        (False, 1),
    ])
    def test_handles_booleans(self, number, result):

        assert number_of_digits(number) == result

    @pytest.mark.parametrize("number, result", [
        (1 + 2j, 0),
    ])
    def test_handles_imaginary_numbers(self, number, result):

        assert number_of_digits(number) == result

    @pytest.mark.parametrize("number, result", [
        (math.inf, 0),
        (math.pi, 1),
        (math.e, 1),
    ])
    def test_handles_special_numbers(self, number, result):

        assert number_of_digits(number) == result
