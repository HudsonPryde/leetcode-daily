def minimumLength(s: str) -> int:
    d = "abcdefghijklmnopqrstuvwxyz"
    res = 0
    for k in d:
        v=s.count(k)
        if v==0:continue
        if v%2==0:
            res += 2
        else:
            res += 1
    
    return res
        