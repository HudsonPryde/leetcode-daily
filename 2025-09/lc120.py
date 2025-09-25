from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}
        return self.helper(triangle,0,0,dp)
    def helper(self, tri, i, j, dp):
        if (i,j) in dp: return dp[(i,j)]
        if i >= len(tri):
            return 0
        dp[(i,j)] = tri[i][j] + min(self.helper(tri,i+1,j),self.helper(tri,i+1,j+1))
        return dp[(i,j)]