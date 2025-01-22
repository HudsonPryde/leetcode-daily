from typing import List


def missingRolls(rolls: List[int], mean: int, n: int) -> List[int]:
    s = sum(rolls)
    target = ((len(rolls)+n)*mean) - s
    k = target//n
    r = target%n
    
    if target < n or target > n*6:
        return []
    
    return [k + (1 if i < r else 0) for i in range(n)]
    


print(missingRolls([1, 3, 5, 2, 6, 4, 3, 2, 5, 1, 6, 4, 2, 3, 5, 1, 4, 6, 2, 5, 3, 6, 1, 4, 5],4,12))