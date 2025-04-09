from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k: return -1
        s = set(nums)
        return len(s)-1 if k in s else len(s)