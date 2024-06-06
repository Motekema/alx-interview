#!/usr/bin/python3
"""
Module for making change with minimum coins
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet a given total amount
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
