from typing import List


def xorAllNums(nums1: List[int], nums2: List[int]) -> int:
    x1 = 0
    if len(nums2)%2==1:
        for a in nums1:
            x1 = x1^a

    x2 = 0
    if len(nums1)%2==1:
        for b in nums2:
            x2 = x2^b
            print(b^x1)
    return x1^x2

print(xorAllNums([1,2],[3,4]))