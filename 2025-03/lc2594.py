from typing import List
import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low, high = 0, max(ranks)*(cars**2)

        def check(mid:int):
            t = 0
            for r in ranks:
                x = math.floor(math.sqrt((mid/r)))
                if x == 0: return False
                t += x
                if t >= cars: return True
            
            return False
                

        while low < high:
            mid = low + (high-low)//2
            if check(mid):
                high = mid
            else:
                low = mid+1
        return low

s = Solution()
print(s.repairCars([4,2,3,1],10))