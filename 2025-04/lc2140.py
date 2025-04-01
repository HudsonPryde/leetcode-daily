from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            p,b = questions[i]
            n_q = i + b + 1
            take = p + (dp[n_q] if n_q < n else 0)
            skip = dp[i+1]
            dp[i] = max(take,skip)
        return dp[0]
    
s = Solution()
print(s.mostPoints([[3,2],[4,3],[4,4],[2,5]]))