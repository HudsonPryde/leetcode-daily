def nearestPalindromic(n: str) -> str:
    even = len(n)%2 == 0
    if int(n) <= 10:
        return str(int(n)-1)
    
    if even:
        half = n[:(len(n)//2)]
        p1 = half + half[::-1]
        inc_half = str(int(half)+1)
        p2 = inc_half + inc_half[len(half)::-1]
        dec_half = str(int(half)-1)
        p3 = dec_half + dec_half[len(half)::-1]
    else:
        half = n[:(len(n)//2)+1]
        p1 = half + half[len(half)-2::-1]
        inc_half = str(int(half)+1)
        p2 = inc_half + inc_half[len(half)-2::-1]
        dec_half = str(int(half)-1)
        p3 = dec_half + dec_half[len(half)-2::-1]
    p4 = "9"*(len(n)-1)
    p5 = "1" + "0"*(len(n)-1) + "1"

    ps = [p1,p2,p3,p4,p5]
    print(ps)
    diff = float("inf")
    n = int(n)
    res = 0
    for p in ps:
        i = int(p)
        if i == n:
            continue
        if abs(i-n) < diff:
            diff = abs(i-n)
            res = i
        elif abs(i-n) == diff:
            if i < res:
                res = i
    return str(res)

print(nearestPalindromic("11011"))