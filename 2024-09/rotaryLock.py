from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    # Write your code here
    time = 0
    curr = 1
    for d in C:
        if d == curr:
            continue
        if d > curr:
            a = abs(d-curr)
            b = N-d+curr
        elif d < curr:
            a = abs(d-curr)
            b = N-curr+d
        time += min(a, b)
        curr = d
    return time
print(getMinCodeEntryTime(10,4,[9,3,4,10]))