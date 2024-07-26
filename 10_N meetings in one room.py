def maxMeetings(start, end, n):
    meetings = sorted(zip(start, end), key=lambda x: x[1])

    count = 0
    last_end_time = -1

    for meeting in meetings:
        if meeting[0] > last_end_time:
            count += 1
            last_end_time = meeting[1]

    return count


# Example usage
n = 6
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
print(maxMeetings(start, end, n))  # Output: 4
