from typing import List


def findTargetSumWays(nums: List[int], target: int) -> int:
    s = sum(nums)
    target = abs(target)
    if s < target or (s-target)%2 == 1:
        return 0
    S = (s-target)//2
    memo = [1] + [0]*S
    for num in nums:
        for i in range(S,-1,-1):
            if i >= num:
                memo[i] += memo[i-num]
    return memo[-1]

print(findTargetSumWays([1,1,1,1,1], 3))