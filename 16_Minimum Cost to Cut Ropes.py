import heapq


def minCostToConnectRopes(arr):
    # Create a min-heap from the list of ropes
    heapq.heapify(arr)

    total_cost = 0

    # While there is more than one rope in the heap
    while len(arr) > 1:
        # Extract the two smallest ropes
        first_min = heapq.heappop(arr)
        second_min = heapq.heappop(arr)

        # The cost to connect these two ropes
        cost = first_min + second_min
        total_cost += cost

        # Insert the new rope back into the heap
        heapq.heappush(arr, cost)

    return total_cost


# Example usage
arr = [4, 3, 2, 6]
print(minCostToConnectRopes(arr))  # Output: 29
