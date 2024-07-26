def minTimeToAssignMiceToHoles(mice, holes):
    # Sort the positions of mice and holes
    mice.sort()
    holes.sort()

    # Calculate the maximum distance required
    max_distance = 0
    for i in range(len(mice)):
        max_distance = max(max_distance, abs(mice[i] - holes[i]))

    return max_distance


# Example usage
N = 3
mice = [4, -4, 2]
holes = [4, 0, 5]

print(minTimeToAssignMiceToHoles(mice, holes))  # Output: 4
