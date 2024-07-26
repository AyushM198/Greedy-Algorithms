def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals based on the start time
    intervals.sort(key=lambda x: (x[0], x[1]))

    merged = []

    for interval in intervals:
        # If the merged list is empty or there is no overlap, add the interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # There is an overlap, merge the current interval with the last one
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


# Example usage
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]
