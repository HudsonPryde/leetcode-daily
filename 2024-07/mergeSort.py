from typing import List


def sortArray(nums: List[int]) -> List[int]:
    nums2 = nums.copy()
    def partition(b, low, high, a):
        if (high - low) <= 1:
            return
        mid = (high + low) // 2
        partition(a, low, mid, b)
        partition(a, mid, high, b)
        merge(b, low, mid, high, a)
    
    def merge(b, low, mid, high, a):
        i, j = low, mid
        for k in range(low, high):
            if i < mid and (j >= high or a[i] <= a[j]):
                b[k] = a[i]
                i += 1
            else:
                b[k] = a[j]
                j += 1
    
    partition(nums, 0, len(nums), nums2)
    print(nums)
        


sortArray([5,2,3,1])
