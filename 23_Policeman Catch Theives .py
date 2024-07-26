def catchThieves(arr, k):
    # Lists to store positions of policemen and thieves
    policemen = []
    thieves = []

    # Traverse the array to fill the positions of policemen and thieves
    for i, char in enumerate(arr):
        if char == 'P':
            policemen.append(i)
        elif char == 'T':
            thieves.append(i)

    # Initialize pointers for policemen and thieves
    p_index = 0
    t_index = 0
    caught = 0

    # Traverse both lists with the two-pointer technique
    while p_index < len(policemen) and t_index < len(thieves):
        if abs(policemen[p_index] - thieves[t_index]) <= k:
            # They can catch this thief
            caught += 1
            p_index += 1
            t_index += 1
        elif policemen[p_index] < thieves[t_index]:
            # Policeman is too far left, move to the next policeman
            p_index += 1
        else:
            # Thief is too far left, move to the next thief
            t_index += 1

    return caught


# Example usage
arr = ['P', 'T', 'T', 'P', 'T']
k = 1
print(catchThieves(arr, k))  # Output: 2
