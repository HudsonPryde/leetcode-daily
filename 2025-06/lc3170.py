from heapq import heappop, heappush
class Solution:
    def clearStars(self, s: str) -> str:
        h = []
        r = set()
        for i,c in enumerate(s):
            if c != "*":
                heappush(h, (c, -i))
            else:
                r.add(-heappop(h)[1])
        return "".join([c for i,c in enumerate(s) if i not in r and c != "*"])

s = Solution()
print(s.clearStars("abc*de*fgh*"))