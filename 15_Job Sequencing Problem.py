def jobScheduling(jobs, n):
    # Sort jobs according to decreasing order of profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find the maximum deadline to determine the size of the timeline
    max_deadline = max(job[1] for job in jobs)

    # Create a timeline to keep track of free time slots
    timeline = [False] * (max_deadline + 1)

    count_jobs = 0
    max_profit = 0

    for job in jobs:
        job_id, deadline, profit = job
        # Find a free time slot for this job
        for t in range(min(max_deadline, deadline), 0, -1):
            if not timeline[t]:
                timeline[t] = True
                count_jobs += 1
                max_profit += profit
                break

    return count_jobs, max_profit


# Example usage
N = 4
jobs = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
print(jobScheduling(jobs, N))  # Output: (2, 60)
