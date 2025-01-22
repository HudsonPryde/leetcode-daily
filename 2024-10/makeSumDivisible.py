from collections import deque
from typing import List


def minSubarray(nums: List[int], p: int) -> int:
    s = sum(nums)
    r = s%p
    if r == 0: return 0
    m = {0:-1}
    l = len(nums)
    c = 0
    for i,n in enumerate(nums):
        c = (c+n)%p
        k = (c-r+p)%p
        if k in m:
            l = min(l, i-m[k])
            if l == 1: return 1
        m[c] = i
        
    if l == len(nums): return -1
    else: return l
                
print(minSubarray([26,19,11,14,18,4,7,1,30,23,19,8,10,6,26,3], 26))
