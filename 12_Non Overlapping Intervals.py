def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    # Sort intervals based on their end time
    intervals.sort(key=lambda x: x[1])

    # Initialize the end time of the last added interval
    end = intervals[0][1]
    count = 0

    # Iterate through the sorted intervals
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            # If the current interval starts before the last interval ends, increment the count
            count += 1
        else:
            # Update the end time to the end of the current interval
            end = intervals[i][1]

    return count


# Example usage
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(eraseOverlapIntervals(intervals))  # Output: 1
