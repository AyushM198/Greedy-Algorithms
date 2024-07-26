def largest_permutation(arr, k):
    n = len(arr)
    # Map each value to its index
    index_map = {value: i for i, value in enumerate(arr)}

    for i in range(n):
        if k <= 0:
            break

        # The largest possible value to be at position i
        largest_value = n - i

        if arr[i] == largest_value:
            continue

        # The index of the largest value that should be at position i
        largest_index = index_map[largest_value]

        # Swap the values in the array
        arr[i], arr[largest_index] = arr[largest_index], arr[i]

        # Update the index map
        index_map[arr[largest_index]] = largest_index
        index_map[arr[i]] = i

        # Decrease the number of swaps available
        k -= 1

    return arr


# Example usage
arr = [4, 2, 3, 1]
k = 2
print(largest_permutation(arr, k))  # Output: [4, 1, 3, 2]
