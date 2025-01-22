def minBitFlips(start: int, goal: int) -> int:
    n1, n2 = format(start, 'b'), format(goal, 'b')
    l = max(len(n1),len(n2))
    n1, n2 = n1.zfill(l), n2.zfill(l)
    print(n1, n2)
    res = 0
    for a,b in zip(n1,n2):
        if a != b:
            res += 1
    return res
print(minBitFlips(10, 7))