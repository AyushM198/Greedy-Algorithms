def min_platforms(arrivals, departures):
    # Sort both arrival and departure arrays
    arrivals.sort()
    departures.sort()

    n = len(arrivals)
    platforms_needed = 1
    max_platforms = 1

    i = 1  # Pointer for arrivals
    j = 0  # Pointer for departures

    while i < n and j < n:
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            i += 1
        else:
            platforms_needed -= 1
            j += 1

        if platforms_needed > max_platforms:
            max_platforms = platforms_needed

    return max_platforms


# Example usage
arrivals = [100, 150, 200, 300, 350, 400]
departures = [200, 300, 400, 500, 450, 600]

print(min_platforms(arrivals, departures))  # Output: 3
