from collections import Counter

def maxScore(s: str) -> int:
    left = Counter({'0':0,'1':0})
    right = Counter(s)
    res = 0
    for x in s:
        right[x] -= 1
        left[x] += 1
        res = max(res, right['1']+left['0'])
    return res

