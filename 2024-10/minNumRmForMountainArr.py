from typing import List


def minimumMountainRemovals(nums: List[int]) -> int:
    n = len(nums)
    d = [nums[0]]
    k = [1]*n
    def helper(l: List[int], n: int) -> int:
        low,high = 0, len(l)
        while low < high:
            mid = low + (high-low)//2
            if l[mid] < n:
                low = mid+1
            else:
                high = mid
        return low
    
    for i in range(1, n):
        idx = helper(d, nums[i])
        if idx == len(d):
            d.append(nums[i])
        else:
            d[idx] = nums[i]
        k[i] = len(d)
    
    h = [1]*n
    g = [nums[-1]]
    for i in range(n-1, -1, -1):
        idx = helper(g, nums[i])
        if idx == len(g):
            g.append(nums[i])
        else:
            g[idx] = nums[i]
        h[i] = len(g)
    h.reverse()

    res = float('inf')
    for i in range(n):
        if k[i] > 1 and h[i] > 1:
            res = min(res, n-k[i]-h[i]+1)

    return res

print(minimumMountainRemovals([1,2,3,4,4,3,2,1]))