from typing import List
from collections import Counter


def kthDistinct(arr: List[str], k: int) -> str:
        c = Counter(arr)
        arr = [x[0] for x in c.items() if x[1] == 1]
        if k <= len(arr): return arr[k-1]
        return ""

print(kthDistinct(["d","b","c","b","c","a"], 2))