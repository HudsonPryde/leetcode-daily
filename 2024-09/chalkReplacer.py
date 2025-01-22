from typing import List


def chalkReplacer(chalk: List[int], k: int) -> int:
    s = sum(chalk)
    k = k%s
    for i in range(len(chalk)):
        if k < chalk[i]:
            return i
        k -= chalk[i]
    return k

print(chalkReplacer([5,1,5],22))