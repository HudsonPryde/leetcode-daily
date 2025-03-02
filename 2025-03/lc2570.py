from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = {}
        m,n = len(nums1),len(nums2)
        for i in range(max(m,n)):
            if i < m:
                d[nums1[i][0]] = d.get(nums1[i][0],0)+nums1[i][1]
            if i < n:
                d[nums2[i][0]] = d.get(nums2[i][0],0)+nums2[i][1]
        res = [[k,v] for k,v in d.items()]
        return sorted(res,key=lambda x: x[0])

s = Solution()
print(s.mergeArrays([[1,2],[2,3],[4,5]],[[1,4],[3,2],[4,1]]))