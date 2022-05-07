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


def buy_and_sell_stock_once(prices: List[int]) -> int:
    """
    Computes highest possible profit when buying and selling a stock once
    :param prices: list of prices for the stock
    :return: highest possible profit
    """
    highest_profit = 0
    for i in range(len(prices)):
        price = prices[i]
        next_prices = prices[i:]
        for j in range(len(next_prices)):
            next_price = next_prices[j]
            if next_price - price > highest_profit:
                highest_profit = next_price - price

    return highest_profit


def buy_and_sell_stock_once_v2(prices: List[int]) -> int:
    """
    Proposed version in the book
    """
    # you can't sell on the 1st day since you don't own the stock yet!
    min_price_so_far = float("inf")
    max_profit = 0

    for price in prices:
        profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)

    return max_profit


def buy_and_sell_stock_twice(prices: List[int]) -> int:
    """
    Solution: https://www.youtube.com/watch?v=ixhHvr7PrU0
    Computes highest possible profit when buying and selling a stock twice
    :param prices: list of prices for the stock
    :return: highest possible profit
    """
    # WIP
    min_price_so_far = float("inf")
    max_profit = 0
    number_of_buys = 0
    price_to_purchases_map = {}
    for price in prices:
        min_price_so_far = min(min_price_so_far, price)
        profit_sell_today = price - min_price_so_far
        if profit_sell_today > max_profit:
            price_to_purchases_map[price] += 1
            min_price_so_far = float("inf")
    breakpoint()
    return max_profit
