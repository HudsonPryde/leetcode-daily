from typing import List


def smallestDistancePair(nums: List[int], k: int) -> int:
    nums.sort()
    n = len(nums)
    
    def search(m:int):
        c,i,j = 0,0,0
        while i < n or j < n:
            while j < n and nums[j] - nums[i] <= m:
                j += 1
            c += j-i-1
            i += 1
        return c >= k
        
    
    l,r = 0, nums[-1]-nums[0]
    while l < r:
        m = l + (r-l)//2
        if search(m):
            r = m
        else:
            l = m+1
    return l

print(smallestDistancePair([1,3,1], 1))