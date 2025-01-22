from typing import List


def findLengthOfShortestSubarray(arr: List[int]) -> int:
    r = len(arr)-1
    while r > 0 and arr[r] >= arr[r-1]:
        r -= 1
    
    res = r
    l = 0
    while l < r and (l == 0 or arr[l-1] <= arr[l]):
        # reduce right array to build left if necessary
        while r < len(arr) and arr[l] > arr[r]:
            r += 1
        # keep min len of arr to remove found so far
        res = min(res, r - l - 1)
        l += 1
    return res


print(findLengthOfShortestSubarray([6,3,10,11,15,20,13,3,18,12]))


