from typing import List
from bisect import bisect_left

def maximumBeauty(items: List[List[int]], queries: List[int]) -> List[int]:
    items.sort()
    max_b = []
    curr_max = 0
    for _,b in items:
        curr_max = max(curr_max, b)
        max_b.append(curr_max)
    res = []
    for q in queries:
        idx = bisect_left(items, [q, float('inf')])-1
        if idx < 0: res.append(0)
        else: res.append(max_b[idx])
    return res
print(maximumBeauty([[571,936],[648,906],[751,308],[165,256],[354,606],[565,560],[238,764],[479,351],[909,267],[215,902],[258,698],[945,805],[108,363],[813,591],[443,262],[863,255],[967,935],[685,582],[898,138]], [269,166,617,1169,1637,393,201,1182,1404,1313]))