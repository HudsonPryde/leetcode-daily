def maximumLength(s: str) -> int:
    s += "0"
    n = len(s)
    d = {}
    # marker for start of substring
    idx = 0
    # find special substrings
    for i in range(1, n):
        if s[i] != s[i-1]:
            sub = s[idx:i]
            for j in range(len(sub)):
                # add all special substrings in this substring to the dict
                d[sub[0]*(j+1)] = d.get(sub[0]*(j+1), 0) + (len(sub)-j)
            idx = i
    # take everything with a count greater than 3
    res = [k for k,v in d.items() if v >= 3]
    if not res: return -1

    return len(sorted(res, key=lambda x: len(x))[-1])

print(maximumLength("aaaa"))
        
