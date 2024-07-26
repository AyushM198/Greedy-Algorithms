import heapq

def max_sum_k_items(arr, k):
    if k > len(arr):
        raise ValueError("k cannot be greater than the number of items in the array")

    min_heap = []

    for num in arr:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heappushpop(min_heap, num)

    return sum(min_heap)

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print(max_sum_k_items(arr, k))  # Output will be the sum of the largest 3 items: 24
