import operator
from typing import List


def frequencySort(nums: List[int]) -> List[int]:
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    freq = sorted(d.items(), key=lambda x: (x[1],-x[0]))
    return [x for xs in freq for x in [xs[0]]*xs[1]]

print(frequencySort([1,1,2,2,2,3]))