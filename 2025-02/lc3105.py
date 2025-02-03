from typing import List


def longestMonotonicSubarray(nums: List[int]) -> int:
    res = 1
    curr = 1
    dir = 1
    n = len(nums)
    for i in range(1, n):
        if nums[i] > nums[i-1]:
            if dir == -1:
                curr = 1
                dir = 1
            curr += 1
        elif nums[i] < nums[i-1]:
            if dir == 1:
                curr = 1
                dir = -1
            curr += 1
        else:
            curr = 1
        res = max(res,curr)
    return res

print(longestMonotonicSubarray([1,4,3,3,2]))
