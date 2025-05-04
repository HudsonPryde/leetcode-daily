from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        res = 0
        for u,v in dominoes:
            if (u,v) in d:
                res += d[(u,v)]
                d[(u,v)] += 1
            elif (v,u) in d:
                res += d[(v,u)]
                d[(v,u)] += 1
            else:
                d[(u,v)] = 1
        return res

s = Solution()
print(s.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))