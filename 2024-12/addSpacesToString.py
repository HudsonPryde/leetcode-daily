from typing import List


def addSpaces(s: str, spaces: List[int]) -> str:
    res = []
    last_idx = 0
    for idx in spaces:
        res.append(s[last_idx:idx])
        last_idx = idx
    res.append(s[last_idx:])
    return " ".join(res)

print(addSpaces("LeetcodeHelpsMeLearn", [0,8,13,15,19]))