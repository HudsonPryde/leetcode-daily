from typing import List
import math

def rangeSum(nums: List[int], n: int, left: int, right: int) -> int:
    arr = []
    for j in range(n):
        arr.append(nums[j])
        for i in range(j+1, n):
            arr.append(arr[-1] + nums[i])
    arr.sort()
    return sum(arr[left-1:right]) % ((pow(10,9))+7)

print(rangeSum([1,2,3,4],4,1,5))