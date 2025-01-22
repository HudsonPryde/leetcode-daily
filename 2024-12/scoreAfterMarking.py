from typing import List

def findScore(nums: List[int]) -> int:
    res= 0 
    n = len(nums)
    sm = sorted(zip(nums,range(n)),reverse=True)
    marked = set()
    while sm:
        v, i = sm.pop()
        if i in marked: continue
        res += v
        marked.update({i-1,i,i+1})
    return res
print(findScore([2,1,3,4,5,2]))