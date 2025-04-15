from typing import List

from sortedcontainers import SortedList

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res, n = 0, len(nums1)
        idxs = [0]*n
        arr = SortedList()
        for i,num in enumerate(nums1):
            idxs[num] = i
        for i,num in enumerate(nums2):
            nums1[i] = idxs[num]
        for i,num in enumerate(nums1[::-1]):
            idx = arr.bisect(num)
            res += (i-idx)*(num-idx)
            arr.add(num)
        return res

s =Solution()
print(s.goodTriplets([1,2,0],[1,0,2]))