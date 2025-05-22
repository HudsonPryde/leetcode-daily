from typing import List
from heapq import heappop, heappush

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        queries.sort(key=lambda x: x[0])
        h = []
        d = [0]*(n+1)
        res = 0
        j = 0
        for i, num in enumerate(nums):
            res += d[i]
            while j < len(queries) and queries[j][0] == i:
                heappush(h, -queries[j][1])
                j += 1
            while res < num and h and -h[0] >= i:
                res += 1
                d[-heappop(h)+1] -= 1
            if res < num:
                return -1
        return len(h)

s = Solution()
print(s.maxRemoval([0,0,1,1,0], [[3,4],[0,2],[2,3]]))