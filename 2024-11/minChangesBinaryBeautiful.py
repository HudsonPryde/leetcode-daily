def minChanges(s: str) -> int:
    res = 0
    for i in range(0,len(s),2):
        if s[i] != s[i+1]:
            res += 1
    return res

print(minChanges("00000000"))
