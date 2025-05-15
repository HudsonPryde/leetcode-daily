from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        prev = None
        for l,g in zip(words,groups):
            if prev == None:
                res.append(l)
                prev = g
                continue
            if prev != g:
                res.append(l)
                prev = g
        return res

s = Solution()
print(s.getLongestSubsequence(["e","a","b"], [0,0,1]))


