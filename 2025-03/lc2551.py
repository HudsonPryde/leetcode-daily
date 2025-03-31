from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairs = [weights[i] + weights[i+1] for i in range(n-1)]
        pairs.sort()
        res = 0
        for i in range(k-1):
            res += pairs[n-2-i] - pairs[i]
        return res

s = Solution()
print(s.putMarbles([1,3,5,1],2))
