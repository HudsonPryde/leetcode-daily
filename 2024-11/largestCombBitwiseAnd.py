from typing import List


def largestCombination(candidates: List[int]) -> int:
    d = [0]*24
    for c in candidates:
        b = bin(c)[:1:-1]
        print(b)
        for i in range(len(b)):
            if b[i] == "1":
                d[i] += 1
    return max(d)

print(largestCombination([10000000,8388608]))