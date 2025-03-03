from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        larger = []
        same = []
        for num in nums:
            if num > pivot:
                larger.append(num)
            elif num < pivot:
                smaller.append(num)
            else:
                same.append(num)
        return smaller + same + larger
s = Solution()
print(s.pivotArray([9,12,5,10,14,3,10], 10))
