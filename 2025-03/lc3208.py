from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors = colors + colors[:k-1]
        res = 0
        prev = colors[0]
        count = 1
        for i in range(1,len(colors)):
            if colors[i] != prev:
                count += 1
            else:
                count = 1
            prev = colors[i]
            if count >= k:
                res += 1
        return res
s = Solution()
print(s.numberOfAlternatingGroups([0,1,0,1],4))