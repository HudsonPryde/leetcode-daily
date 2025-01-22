from collections import Counter

def canMakeSubsequence(str1: str, str2: str) -> bool:
    # use 2 pointers increase p1 until it equals value at p2 or value at p2 -1 increase p2
    res = 0
    n,m = len(str1), len(str2)
    for i in range(n):
        if res < m and (ord(str2[res]) - ord(str1[i]))%26 <= 1:
            res += 1
            if res == m:
                return True
    return False
    

print(canMakeSubsequence("eao", "ofa"))