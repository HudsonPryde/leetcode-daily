from typing import List


def sortPeople(names: List[str], heights: List[int]) -> List[str]:
    names = sorted(zip(heights, names), reverse=True)
    return [name[1] for name in names]

print(sortPeople(["Mary","John","Emma"], [180,165,170]))