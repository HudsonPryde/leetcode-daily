from typing import List


def finalPrices(prices: List[int]) -> List[int]:
    q=[]
    res = prices[:]
    for i,p in enumerate(prices):
        while q and prices[q[-1]] >= p:
            res[q.pop()]-=p
        q.append(i)
    return res
print(finalPrices([8,4,6,2,3]))