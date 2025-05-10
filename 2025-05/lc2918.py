from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1,z2 = nums1.count(0), nums2.count(0)
        s1,s2 = sum(nums1), sum(nums2)
        target = max(s1+z1,s2+z2)
        if target == s1+z1:
            if s1+z1!=s2+z2 and z2 == 0: return -1
            return target
        else:
            if s1+z1!=s2+z2 and z1 == 0: return -1
            return target
        
        

s = Solution()
print(s.minSum([3,2,0,1,0],[6,5,0]))