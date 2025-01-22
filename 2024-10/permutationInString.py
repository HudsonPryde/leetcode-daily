from collections import Counter
def checkInclusion(s1: str, s2: str) -> bool:
    k1,k2 = [0]*26, [0]*26
    n1,n2 = len(s1), len(s2)
    if n1>n2: return False
    for i in range(n1):
        k1[ord(s1[i])-97]+=1
        k2[ord(s2[i])-97]+=1
    if k1==k2: return True
    for i in range(n1,n2):
        k2[ord(s2[i])-97]+=1
        k2[ord(s2[i-n1])-97]-=1
        if k1==k2: return True
    return False
    

print(checkInclusion("hello", "ooolleoooleh"))