def getLucky(s: str, k: int) -> int:
    alph = list('abcdefghijklmnopqrstuvwxyz')
    d = {a:i for i,a in enumerate(alph)}
    c = "".join([str(d[a]+1) for a in list(s)])
    for _ in range(k-1):
        t = list(str(c))
        if len(t) == 1:
            return int(c)
        c = sum([int(x) for x in t])
    return int(c)
print(getLucky("leetcode", 2))