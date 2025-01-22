from typing import List
from heapq import heappush, heapreplace, nlargest

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        for num in nums:
            if len(self.nums) >= self.k:
                if num > self.nums[0]:
                    heapreplace(self.nums, num)
            else:
                heappush(self.nums, num)

    def add(self, val: int) -> int:
        if len(self.nums) >= self.k:
            if val > self.nums[0]:
                heapreplace(self.nums, val)
        else:
            heappush(self.nums, val)
        return self.nums[0]

o = KthLargest(3, [4,5,8,2])
vals = [3,5,10,9,4]
for val in vals:
    print(o.add(val))