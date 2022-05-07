import pytest

from algorithms.stock_prices import buy_and_sell_stock_once, buy_and_sell_stock_once_v2, buy_and_sell_stock_twice


@pytest.mark.parametrize("prices, expected_highest_profit", [
    ([22, 25, 28, 27], 6),
    ([22, 19, 22, 17], 3),
    ([22, 19, 18, 12], 0),
    ([20, 19, 18, 12, 13, 19, 11], 7),
    ([1, 2, 100], 99),
    ([310, 315, 275, 295, 260, 270, 290, 230, 255, 250], 30),
])
def test_returns_highest_profit_when_buying_and_selling_one_time(prices, expected_highest_profit):
    assert buy_and_sell_stock_once(prices) == expected_highest_profit
    assert buy_and_sell_stock_once_v2(prices) == expected_highest_profit


@pytest.mark.parametrize("prices, expected_highest_profit", [
    ([1, 2, 100], 197),  # failing test case
])
def test_returns_highest_profit_when_buying_and_selling_two_times(prices, expected_highest_profit):
    assert buy_and_sell_stock_twice(prices) == expected_highest_profit
