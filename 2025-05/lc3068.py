from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # trick: any two nodes can be XOR'd without changing the rest of the graph
        n = len(nums)
        deltas = [(x^k)-x for x in nums]
        candidates = [d for d in deltas if d >= 0]
        if len(candidates) % 2 == 0:
            return sum(nums) + sum(candidates)
        
        minCan = min(candidates)
        maxNeg = max((d for d in deltas if d < 0), default=float('-inf'))

        return sum(nums) + max(sum(candidates)+maxNeg, sum(candidates)-minCan)
    
s = Solution()
print(s.maximumValueSum([1,2,1], 3, []))