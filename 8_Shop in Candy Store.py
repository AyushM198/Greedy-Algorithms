def candyStore(candies, N, K):
    candies.sort()

    # Calculate the minimum cost
    min_cost = 0
    i = 0
    while i < N:
        min_cost += candies[i]
        i += (K + 1)

    # Calculate the maximum cost
    max_cost = 0
    i = N - 1
    while i >= 0:
        max_cost += candies[i]
        i -= (K + 1)

    return min_cost, max_cost


# Example usage
N = 5
K = 4
candies = [3, 2, 1, 4, 5]

print(candyStore(candies, N, K))  # Output: (1, 5)
