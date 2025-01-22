from heapq import heappush, heappop
from collections import deque

def minimumSteps(s: str) -> int:
    n = len(s)
    pos = deque()
    total_swaps = 0
    for i in range(n-1, -1, -1):
        if s[i] == "0":
            pos.append(i)
        elif pos and s[i] == "1":
            p = pos.popleft()
            total_swaps += p-i
            pos.append(i)
    return total_swaps

def minimumStepsV2(s: str) -> int:
    total_swaps = 0
    b = 0
    for i in s:
        if i == "1":
            b += 1
        else:
            total_swaps += b
    return total_swaps


print(minimumStepsV2("101"))
