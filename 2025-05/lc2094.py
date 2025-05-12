from typing import List
from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits = {x:digits.count(x) for x in list(set(digits))}
        res = []
        for num in range(100,1000):
            if num%2 != 0: continue
            s = list(str(num))
            d = {int(x):s.count(x) for x in list(set(s))}
            valid = True
            for k,v in d.items():
                if k not in digits or digits[k] < v:
                    valid = False
                    break
            if valid:
                res.append(num) 
        return res

s = Solution()
print(s.findEvenNumbers([2,1,3,0]))