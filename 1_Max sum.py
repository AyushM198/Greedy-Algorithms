def max_sum_with_k_elements(arr, k):
    arr.sort(reverse=True)

    max_sum = sum(arr[:k])

    return max_sum

arr = [5, 2, 1, 6, 3]
k = 3
result = max_sum_with_k_elements(arr, k)
print("Maximum sum of", k, "elements:", result)
