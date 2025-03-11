class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        pos = [-1,-1,-1]
        for i in range(n):
            pos[ord(s[i])-ord('a')]=i
            if -1 not in pos:
                res += 1 + min(pos)
        return res

s =Solution()
print(s.numberOfSubstrings('abcabc'))

            