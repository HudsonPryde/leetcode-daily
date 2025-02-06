from typing import List


def tupleSameProduct(nums: List[int]) -> int:
    d = {}
    n = len(nums)
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            x = nums[i]*nums[j]
            if x not in d:
                d[x] = 1
            else:
                res += d[x]*8
                d[x] += 1
    return res
print(tupleSameProduct([1,2,4,8,16,32]))