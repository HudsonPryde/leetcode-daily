from typing import List


def mincostTickets(days: List[int], costs: List[int]) -> int:
    max_day = max(days)
    travel_days = set(days)
    dp = [0]*(max_day+1)
    for i in range(1,max_day+1):
        if i in travel_days:
            p1 = dp[i-1]+costs[0] if i-1 >= 0 else costs[0]
            p2 = dp[i-7]+costs[1] if i-7 >= 0 else costs[1]
            p3 = dp[i-30]+costs[2] if i-30 >= 0 else costs[2]
            dp[i] = min(p1,p2,p3)
        else:
            dp[i] = dp[i-1]
    return dp[-1]

print(mincostTickets([50, 82, 91, 104, 120, 137, 268, 339, 362, 365],[675, 848, 594]))

