def minSteps(n: int) -> int:
    s = 1
    res = 0
    prev = 0
    while s < n:
        if n%s == 0 and s*2 <= n:
            prev = s
            s *= 2
            res += 1
        else:
            s += prev
        res += 1
    return res

print(minSteps(1))