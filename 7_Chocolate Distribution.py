def find_min_diff(A, N, M):
    # If there are no students or no packets
    if M == 0 or N == 0:
        return 0

    # Sort the given packets
    A.sort()

    # Number of students cannot be more than number of packets
    if N < M:
        return -1

    # Initialize the minimum difference as a large number
    min_diff = float('inf')

    # Find the minimum difference
    for i in range(N - M + 1):
        diff = A[i + M - 1] - A[i]
        if diff < min_diff:
            min_diff = diff

    return min_diff


# Example usage:
N = 8
M = 5
A = [3, 4, 1, 9, 56, 7, 9, 12]
print(find_min_diff(A, N, M))  # Output: 6
