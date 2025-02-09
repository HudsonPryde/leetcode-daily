import math
from typing import List
from collections import defaultdict


def countBadPairs(nums: List[int]) -> int:
    n = len(nums)
    res = 0
    d= defaultdict(int)
    for i in range(n):
        s = nums[i]-i
        if s in d:
            res += d[s]
        d[s] += 1
    return math.comb(len(nums), 2) - res

print(countBadPairs([4,1,3,3]))