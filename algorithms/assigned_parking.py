"""
There are n cars located on a 2-dimensional plane at positions (x[i], y[i])
where 0<= i <= n. They need to be parked in a straight line parallel to the
x-axis with no spaces between them. The fuel consumed to move a car is
abs(x[finish] - x[start]) + abs(y[finish] - y[start]). Determine the minimum
fuel cost to arrange the cars side-by-side in a row parallel to the x-axis.

Example:
2 cars, one at (1, 1) and another one at (4, 4  )
x = [1, 4]
y = [1, 4]

Optimal solution:
 - Car at (1, 1) moves to (3, 1) for a cost of  abs(3-1) + abs(1-1) = 2
 - Car at (4, 4) moves to (4, 1) for a cost of 0 + 3 = 3

 Total fuel consumed = 2 + 3 = 5

"""
from typing import List


def get_fuel_consumption(x: List, y: List) -> int:
    finish = 1
    start = 0
    return abs(x[finish] - x[start]) + abs(y[finish] - y[start])


def find_target_coordinates(x, y) -> List:
    breakpoint()


def min_fuel(x, y) -> int:
    # find target coordinates and calculate fuel consumption
    breakpoint()
    # both cars must have same x
    pass
