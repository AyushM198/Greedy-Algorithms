def fractional_knapsack(n, w, value, weight):
    # List to store (value, weight, value-to-weight ratio) for each item
    items = []
    for i in range(n):
        items.append((value[i], weight[i], value[i] / weight[i]))

    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0.0
    remaining_capacity = w

    for val, wt, ratio in items:
        if remaining_capacity == 0:
            break
        if wt <= remaining_capacity:
            total_value += val
            remaining_capacity -= wt
        else:
            total_value += ratio * remaining_capacity
            remaining_capacity = 0

    return total_value


n = 3
w = 50
value = [60, 100, 120]
weight = [10, 20, 30]
print(fractional_knapsack(n, w, value, weight))
