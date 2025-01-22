from typing import List


def shiftingLetters(s: str, shifts: List[List[int]]) -> str:
    d = [0]*(len(s)+1)
    for start,end,dir in shifts:
        x = 1 if dir == 1 else -1
        d[start] += x
        d[end+1] -= x
    k = 0
    res = ""
    for i in range(len(s)):
        k += d[i]
        c = (((ord(s[i])+k)-97)%26)+97
        res += chr(c)
    return res


print(shiftingLetters("dztz", [[0,0,0],[1,1,1]]))
