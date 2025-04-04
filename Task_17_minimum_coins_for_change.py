def find_minimum_coins_for_change(n, coins):
    change = 0
    for coin in coins[::-1]:
        if n == 0:
            break

        res = n // coin
        if res != 0:
            change += res
            n = n - coin * res

    if n != 0:
        return -1
    return change