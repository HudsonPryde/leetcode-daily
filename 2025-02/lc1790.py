from collections import Counter
def areAlmostEqual(s1: str, s2: str) -> bool:
    if s1 == s2: return True
    set1 = Counter(s1)
    set2 = Counter(s2)
    if set1 != set2: return False
    n = len(s2)
    count = 0
    for i in range(n):
        if s1[i] != s2[i]:
            count += 1
    return count == 2

print(areAlmostEqual("bank","kanb"))
