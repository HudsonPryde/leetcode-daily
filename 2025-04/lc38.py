class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self._helper(2, "1", n)
    def _helper(self, n:int, s:str, k:int) -> str:
        new_s = ""
        cur,cnt = None,0
        for i in range(len(s)):
            num = s[i]
            if not cur:
                cur, cnt = num,1
            elif num == cur:
                cnt += 1
            elif num != cur:
                new_s += str(cnt)+s[i-1]
                cur,cnt = num,1
            if i == len(s)-1:
                new_s += str(cnt)+num
        if n == k:
            return new_s
        else:
            return self._helper(n+1, new_s, k)

s = Solution()
print(s.countAndSay(4))