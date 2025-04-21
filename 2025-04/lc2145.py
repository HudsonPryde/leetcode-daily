from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prev = lower
        high,low = lower,lower
        for dif in differences:
            prev+=dif
            high = max(high,prev)
            low = min(low,prev)
        high += (lower-low)
        res = upper-high
        return res+1 if res >= 0 else 0

s =Solution()
print(s.numberOfArrays([4,-7,2],3,6))