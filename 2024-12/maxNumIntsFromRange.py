from typing import List


def maxCount(banned: List[int], n: int, maxSum: int) -> int:
    banned = set(banned)
    
    nums = list(set(range(1,n+1))-banned)
    total = sum(nums)
    while total > maxSum:
        total -= nums.pop()
    return len(nums)
print(maxCount([12,12],13, 2199))