def punishmentNumber(n: int) -> int:
    def helper(num: str, t: int):
        if num == '' and t == 0:
            return True
        for i in range(1, len(num)+1):
            if helper(num[i:], t-int(num[:i])):
                return True
        return False
    res = 0
    for i in range(1, n+1):
        sq = i*i
        if helper(str(sq), i):
            res += sq
    return res
    
print(punishmentNumber(10))