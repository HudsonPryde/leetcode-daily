def findKthBit(n: int, k: int) -> str:
    s = "0"
    for i in range(n):
        s += "1" + bin(int(s,2)^(2**(len(s)+1)-1))[:2:-1]
        if len(s) > k:
            return s[k-1]
    return s[k-1]

print(findKthBit(4,12))