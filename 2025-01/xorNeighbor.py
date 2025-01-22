from typing import List


def doesValidArrayExist(derived: List[int]) -> bool:
    return sum(derived)%2 == 0
print(doesValidArrayExist([1,0]))