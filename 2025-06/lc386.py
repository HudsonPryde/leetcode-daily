from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        x = 1
        res = []
        for _ in range(n):
            res.append(x)
            if x *10 <= n:
                x *= 10
            else:
                if x >= n:
                    x //= 10
                x += 1
                while x%10 ==0:
                    x //= 10
        return res


s = Solution()
print(s.lexicalOrder(20))