def merge(intervals):
    if not intervals:
        return []

    # Sort intervals based on their start times
    intervals.sort(key=lambda x: x[0])

    merged = []

    for interval in intervals:
        # If merged list is empty or there is no overlap with the last interval in merged
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Merge the current interval with the last interval in merged
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


# Example usage
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]
