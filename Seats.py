def min_seats_required(n):
    # Each person needs a seat and we need at least one seat between each pair of people
    return 2 * n - 1

# Example usage
n = 5
print(min_seats_required(n))  # Output: 9
