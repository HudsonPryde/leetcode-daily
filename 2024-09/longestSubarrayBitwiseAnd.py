from typing import List
from heapq import heappush


def longestSubarray(nums: List[int]) -> int:
    res = []
    count = 1
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            heappush(res, (-nums[i-1], count))
            count = 1
        else:
            count += 1
        if i == len(nums)-1:
            heappush(res, (-nums[i], count))
    return res[0][1]

def longestSubarrayV2(nums: List[int]) -> int:
    n = len(nums)
    max_num = nums[0]
    max_len = 1
    curr_len = 1
    for i in range(1, n):
        if nums[i] > max_num:
            max_num = nums[i]
            max_len = 1
            curr_len = 1
        elif nums[i] == max_num:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 0
    return max_len


print(longestSubarrayV2([1,1,1,1,1,1,2,2]))