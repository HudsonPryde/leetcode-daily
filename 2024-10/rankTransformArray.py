from typing import List


def arrayRankTransform(arr: List[int]) -> List[int]:
    m = {x:i+1 for i,x in enumerate(sorted(list(set(arr))))}
    return [m[a] for a in arr]

print(arrayRankTransform([100,100,100]))