from typing import Counter


class Solution:
    def robotWithString(self, s: str) -> str:
        c = Counter(s)
        stack = []
        res = ""
        k = min(c.keys())
        for i in range(len(s)):
            while stack and k >= stack[-1]:
                res += stack.pop()
            if s[i] == k:
                res += k
                c[k] -= 1
                if c[k] == 0:
                    c.pop(k)
                    k = min(c.keys(),default=None)
            else:
                stack += s[i]
                c[s[i]] -= 1
                if c[s[i]] == 0:
                    c.pop(s[i])
        return res + "".join(stack[::-1])

s = Solution()
print(s.robotWithString("bdda"))
