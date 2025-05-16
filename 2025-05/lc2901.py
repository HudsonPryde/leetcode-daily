from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dp = {}
        res = []
        for i,w in enumerate(words):
            if w in dp:
                res = max(res,dp[w], key=lambda x: len(x))
            else:
                res = max(res, self._helper(i,words,groups,dp,[words[i]]), key=lambda x: len(x))
        return res
    def _helper(self, idx: int, words: List[str], groups: List[int], dp: dict, seq: list[int]):
        if idx in dp:
            return dp[idx]
        max_seq = []
        for j in range(idx+1, len(words)):
            if len(words[idx]) == len(words[j]) and groups[idx] != groups[j]:
                if len([x for i,x in enumerate(words[idx]) if x!=words[j][i]]) <= 1:
                    max_seq = max(max_seq, self._helper(j,words,groups,dp,[words[j]]), key=lambda x: len(x))
        dp[idx] = [words[idx]]+max_seq
        return dp[idx]
        
    
s = Solution()
print(s.getWordsInLongestSubsequence(["dba","db","cc","aa","ac","da","bc","dda","bb","abb","cd","cad","bdd","ca"],[2,7,14,4,9,9,5,9,11,12,7,8,8,3]))
        