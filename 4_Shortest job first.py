def averageWaitingTime(n, bt):
    bt.sort()

    waiting_time = 0
    total_waiting_time = 0

    for i in range(n):
        total_waiting_time += waiting_time
        waiting_time += bt[i]

    avg_waiting_time = total_waiting_time // n

    return avg_waiting_time


n = 5
bt = [4, 3, 7, 2, 9]
print(averageWaitingTime(n, bt))
