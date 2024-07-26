def findPlatform(arr, dep):
    # Sort arrival and departure times
    arr.sort()
    dep.sort()

    n = len(arr)
    platforms_needed = 0
    max_platforms = 0

    # Initialize pointers for arrival and departure
    i = 0
    j = 0

    while i < n and j < n:
        if arr[i] <= dep[j]:
            # New train arrives
            platforms_needed += 1
            i += 1
            max_platforms = max(max_platforms, platforms_needed)
        else:
            # Train departs
            platforms_needed -= 1
            j += 1

    return max_platforms


# Example usage
arr = ["09:00", "09:40", "09:50", "11:00", "15:00", "18:00"]
dep = ["09:10", "11:20", "11:30", "12:00", "19:00", "20:00"]


# Convert time strings to comparable integers (e.g., minutes since midnight)
def time_to_minutes(time_str):
    h, m = map(int, time_str.split(":"))
    return h * 60 + m


# Convert times
arr = [time_to_minutes(t) for t in arr]
dep = [time_to_minutes(t) for t in dep]

print(findPlatform(arr, dep))  # Output: 3
