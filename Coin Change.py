def coin_change(coins, amount):
    # Initialize the dp array with a large number
    dp = [float('inf')] * (amount + 1)
    # Base case: 0 coins are needed to make amount 0
    dp[0] = 0

    # Iterate over each coin
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[amount] is still infinity, return -1 indicating no solution
    return dp[amount] if dp[amount] != float('inf') else -1


# Example usage
coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))  # Output: 3 (11 = 5 + 5 + 1)

coins = [2]
amount = 3
print(coin_change(coins, amount))  # Output: -1 (3 cannot be made with only 2s)
