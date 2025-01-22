from typing import List


def occurrencesOfElement(nums: List[int], queries: List[int], x: int) -> List[int]:
    a = []
    for i in range(len(nums)):
        if nums[i] == x:
            a.append(i)
    return [a[x] if x<len(a) else -1 for x in queries]