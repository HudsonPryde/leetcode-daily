from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # n sides, each vertex in int, v in values is ith vertex: clockwise
        # divide polygon into triangles using verticies of original polygon
        # n-2 triangles are made
        # weight of each triangle is product of its verticies
        # total score is sum of weights
        # find min score
        
        n = len(values)
        dp = [[0]*n for _ in range(n)]
        for l in range(2,n):
            for i in range(n-l):
                j = i+l
                dp[i][j] = min(dp[i][k]+dp[k][j]+values[i]*values[k]*values[j] for k in range(i+1,j))
        return dp[0][n-1]    
print(Solution().minScoreTriangulation([1,3,1,4,1,5]))