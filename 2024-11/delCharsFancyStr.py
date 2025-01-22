def makeFancyString(s: str) -> str:
    res = []
    count = 1
    prev = None
    for c in s:
        if c == prev:
            count += 1
        else:
            count = 1
        prev = c
        if count < 3:
            res.append(c)
    return ''.join(res)


print(makeFancyString('leeetcode'))