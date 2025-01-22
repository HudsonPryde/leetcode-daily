from typing import List


def resultsArray(nums: List[int], k: int) -> List[int]:
    if k == 1: return nums
    n = len(nums)
    res = []
    l,r = 0, 1

    while r < n:
        if nums[r] - nums[r-1] != 1:
            while l < r and l+k -1 < n:
                res.append(-1)
                l += 1
            l = r
        elif r-l == k -1:
            res.append(nums[r])
            l += 1
        r += 1
    return res

print(resultsArray([1,4], 1))
