import math
def minimumDaysToBuyFood(S, N, M):
    total_food_needed = M * S

    sundays = S // 7

    buying_days = S - sundays

    max_food_buyable = N * buying_days

    if max_food_buyable < total_food_needed:
        return -1

    min_buying_days = math.ceil(total_food_needed / N)

    return min_buying_days

S = 45
N = 16
M = 2
print(minimumDaysToBuyFood(S, N, M))
