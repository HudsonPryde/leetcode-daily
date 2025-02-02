from typing import List
from collections import deque

def check(nums: List[int]) -> bool:
    nums = deque(nums)
    n = len(nums)
    s = deque(sorted(nums))
    for _ in range(n):
        if s == nums: return True
        s.appendleft(s.pop())
    return False
print(check([3,4,5,1,2]))