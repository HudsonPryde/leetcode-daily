from typing import List


def countConsistentStrings(allowed: str, words: List[str]) -> int:
    allowed = set(allowed)
    res = 0
    for word in words:
        if set(word).issubset(allowed):
            res += 1
    return res