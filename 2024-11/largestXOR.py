from typing import List


def getMaximumXor(nums: List[int], maximumBit: int) -> List[int]:
    s = []
    t = None
    g = (2**maximumBit)-1
    for n in nums:
        if not t:
            t = n
        else:
            t = t^n
        s.append((g^t))
    return s[::-1]

print(getMaximumXor([0,1,1,3], 2))