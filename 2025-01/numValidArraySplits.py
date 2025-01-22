from typing import List


def waysToSplitArray(nums: List[int]) -> int:
    n = len(nums)
    t = sum(nums)
    res = 0
    curr_t = 0
    for i in range(n-1):
        curr_t += nums[i]
        if curr_t >= (t-curr_t):
            res += 1
    return res

print(waysToSplitArray([6,-1,9]))

