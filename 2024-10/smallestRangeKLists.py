from heapq import heapify, heappop, heappush, heapreplace
from typing import List


def smallestRange(nums: List[List[int]]) -> List[int]:
    n = len(nums)
    heap = []
    for i in range(n):
        for k in nums[i]:
            heappush(heap, (k, i))
    t = set()
    s = [0]*n
    res = []
    while heap:
        k, i = heappop(heap)
        s[i] = k
        t.add(i)
        if len(t) == n:
            max_k = max(s)
            min_k = min(s)
            heappush(res, (abs(max_k-min_k), [min_k,max_k]))
    return heappop(res)[1]

def smallestRangeV2(nums: List[List[int]]) -> List[int]:
    n = len(nums)
    min_range = []
    heap = [(k[0], i) for i,k in enumerate(nums)]
    max_k = max(heap)[0]
    heapify(heap)
    i = heap[0][1]
    while nums[i] and heap:
        min_k, i = heappop(heap)
        if not min_range or abs(max_k-min_k) < abs(min_range[1]-min_range[0]):
            min_range = [min_k, max_k]
        new_k = nums[i].pop(0)
        max_k = max(max_k, new_k)
        heappush(heap, (new_k, i))

    return min_range

print(smallestRangeV2([[-38,15,17,18],[-34,46,58,59,61],[-55,-31,-13,64,82,82,83,84,85],[-3,63,70,90],[2,6,10,28,28,32,32,32,33],[-23,82,88,88,88,89],[33,60,72,74,75],[-5,44,44,57,58,58,60],[-29,-22,-4,-4,17,18,19,19,19,20],[22,57,82,89,93,94],[24,38,45],[-100,-56,41,49,50,53,53,54],[-76,-69,-66,-53,-27,-1,9,29,31,32,32,32,34],[22,47,56],[-34,-28,7,44]]))