from typing import List


def dividePlayers(skill: List[int]) -> int:
    n = len(skill)
    skill.sort()
    chem = 0
    target = skill[0]+skill[-1]
    for a,b in zip(skill[:n//2], reversed(skill[n//2:])):
        if a+b != target: return -1
        chem += a*b
    return chem