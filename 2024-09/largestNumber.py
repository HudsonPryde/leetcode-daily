from typing import List
from functools import cmp_to_key

def largestNumber(nums: List[int]) -> str:
    nums = [str(x) for x in nums]
    def comp(a, b):
        s1, s2 = str(a), str(b)
        if s1+s2 > s2+s1:
            return -1
        else:
            return 1
    nums = sorted(nums, key=cmp_to_key(comp))
    return nums

print(largestNumber([3,30,34,5,9]))