from typing import List

def max_profit(prices: List[int]) -> int:
    min = prices[0]
    profit = 0

    for price in prices:
        temp = price - min
        if temp > profit:
            profit = temp

        if price < min:
            min = price

    return profit