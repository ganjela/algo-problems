"""
1. The min variable is used to track the lowest price encountered so far. This
ensures we always buy at the lowest price before any higher price.

2. The profit keeps track of the highest profit so far. By
iterating through the list of prices, for each price:

The difference between the current price and the lowest price is
calculated to see if it has a higher profit.
If the new profit exceeds the current profit, we update the
profit.

3. If the current price is lower than the current min, we update min to maintain
the lowest price seen so far.
"""

def max_profit(prices):
    min = prices[0]
    profit = 0

    for price in prices:
        temp = price - min
        if temp > profit:
            profit = temp

        if price < min:
            min = price

    return profit