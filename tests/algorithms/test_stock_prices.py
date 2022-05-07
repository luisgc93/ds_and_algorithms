import pytest

from algorithms.stock_prices import calculate_highest_profit


@pytest.mark.parametrize("start_prices, expected_highest_profit", [
    ([22, 25, 28, 27], 6),
    ([22, 19, 22, 17], 3),
    ([22, 19, 18, 12], 0),
    ([20, 19, 18, 12, 13, 19, 11], 7),
    ([1, 2, 2, 100], 95),  # failing test case
])
def test_returns_highest_profit_from_start_prices_list(start_prices, expected_highest_profit):
    assert calculate_highest_profit(start_prices) == expected_highest_profit
