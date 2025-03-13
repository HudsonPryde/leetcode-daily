from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n,m = len(nums),len(queries)
        diff= [0]*(n+1)
        curr = 0
        q = queries[::-1]
        for i,val in enumerate(nums):
            curr += diff[i]
            while q and curr < val:
                l,r,x = q.pop()
                if r >= i:
                    if l > i:
                        diff[l] += x
                    else:
                        curr += x
                    diff[r+1] -= x
            if curr < val:
                return -1
        return m-len(q)
s = Solution()
print(s.minZeroArray([7,6,8],[[0,0,2],[0,1,5],[2,2,5],[0,2,4]]))