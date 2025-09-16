from typing import List
import math
from collections import deque
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        arr = deque(nums)
        res = []
        while arr:
            x = arr.popleft()
            if len(arr) == 0:
                while res:
                    h = res.pop()
                    if math.gcd(x,h) > 1:
                        x = math.lcm(x,h)
                    else:
                        res.append(h)
                        break
                res.append(x)
                break
            y = arr.popleft()
            if math.gcd(x,y) > 1:
                arr.appendleft(math.lcm(x,y))
            else:
                while res:
                    h = res.pop()
                    if math.gcd(x,h) > 1:
                        x = math.lcm(x,h)
                    else:
                        res.append(h)
                        break
                res.append(x)
                arr.appendleft(y)
        return res

print(Solution().replaceNonCoprimes([287,41,49,287,899,23,23,20677,5,825]))

