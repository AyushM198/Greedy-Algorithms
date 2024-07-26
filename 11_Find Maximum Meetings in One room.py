def maxMeetings(start, end, n):
    # Combine the start and end times with their original indices
    meetings = sorted([(start[i], end[i], i) for i in range(n)], key=lambda x: x[1])

    # Initialize the list of selected meetings
    selected_meetings = []

    # Initialize the end time of the last selected meeting
    last_end_time = -1

    # Iterate through the sorted meetings
    for meeting in meetings:
        # If the start time of the current meeting is after the end time of the last selected meeting
        if meeting[0] > last_end_time:
            # Select the current meeting
            selected_meetings.append(meeting[2] + 1)  # Adding 1 to make it 1-based index
            # Update the end time of the last selected meeting
            last_end_time = meeting[1]

    # Print the indices of the selected meetings
    print(" ".join(map(str, sorted(selected_meetings))))


# Example usage
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
n = len(start)
maxMeetings(start, end, n)  # Output: 1 2 4 5

