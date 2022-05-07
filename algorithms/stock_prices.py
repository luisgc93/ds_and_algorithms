"""
** Taken from Elements of Programming Interviews in Python **
Design an algorithm that determines the maximum profit that could
have been made by buying and then selling a single share over a
given day range, subject to the constraint that the buy and the
sell have to take place at the start of the day. (This algorithm
may be needed to backtest a trading strategy.)

* If you try a few test cases, you will see that the  minimum can
occur after the maximum, which violates the requirement in the
problem statement-you have to buy before you can sell.
"""

from typing import List


def calculate_highest_profit(start_prices: List[int]) -> int:
    # TODO: fix algorithm to handle buys at multiple prices
    highest_profit = 0
    for i in range(len(start_prices)):
        price = start_prices[i]
        next_prices = start_prices[i:]
        for j in range(len(next_prices)):
            next_price = next_prices[j]
            if next_price - price > highest_profit:
                highest_profit = next_price - price

    return highest_profit
