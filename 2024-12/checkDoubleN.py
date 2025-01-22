from typing import List


def checkIfExist(arr: List[int]) -> bool:
    doubles = set()
    for x in arr:
        if x*2 in doubles or x/2 in doubles: return True
        doubles.add(x)
    return False
print(checkIfExist([10,2,5,3]))