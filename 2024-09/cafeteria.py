from typing import List


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Sort the list of existing diners
    S.sort()
    
    # Count how many additional diners we can fit
    additional_diners = 0
    
    # 1. Check the gap before the first diner
    first_gap = S[0] - 1
    if first_gap > 0:
        additional_diners += first_gap // (K + 1)
    
    # 2. Check the gaps between diners
    for i in range(1, M):
        gap = S[i] - S[i - 1] - 1
        if gap > 0:
            additional_diners += (gap - K) // (K + 1) if gap > K else 0
    
    # 3. Check the gap after the last diner
    last_gap = N - S[-1]
    if last_gap > 0:
        additional_diners += last_gap // (K + 1)
    
    return additional_diners

print(getMaxAdditionalDinersCount(10,1,2,[2,6]))
print(getMaxAdditionalDinersCount(15,2,3,[11,6,14]))
# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
# o,o,o,o,o,x,o,o,o,o,,x,,o,,o,,x,,o,
# o,o,i,o,o,x,o,o,o,o,,x,,o,,o,,x,,o,