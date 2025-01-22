def findTheLongestSubstring(s: str) -> int:
    count = [-2]*32
    count[0] = -1
    res = 0
    mask = 0
    for i, c in enumerate(s):
        if c == 'a':
            mask ^= 1
        elif  c == 'e':
            mask ^= 2
        elif c == 'i':
            mask ^= 4
        elif c == 'o':
            mask ^= 8
        elif c == 'u':
            mask ^= 16
        
        prev = count[mask]
        if prev == -2:
            count[mask] = i
        else:
            res = max(res, i-prev)
    return res
print(findTheLongestSubstring("eleetminicoworoep"))