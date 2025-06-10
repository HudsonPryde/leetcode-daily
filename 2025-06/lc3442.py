from typing import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        max_odd = 0
        min_even = float('inf')
        for v in c.values():
            if v % 2 == 0:
                min_even = min(min_even, v)
            else:
                max_odd = max(max_odd, v)
        return max_odd-min_even