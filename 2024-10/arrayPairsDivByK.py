from typing import List


def canArrange(arr: List[int], k: int) -> bool:
    m = {}
    pairs = 0
    for a in arr:
        if a%k in m:
            if m[a%k] > 0:
                m[a%k] -= 1
                pairs += 1
                continue
        if k - a%k in m:
            if a%k == 0:
                if m[k - a%k] > 0:
                    m[k - a%k] -= 1
                    pairs += 1
                    continue
            m[k - a%k] += 1
        else:
            m[k - a%k] = 1
    return pairs == len(arr)//2

print(canArrange([1,2,3,4,5,10,6,7,8,9], 5))