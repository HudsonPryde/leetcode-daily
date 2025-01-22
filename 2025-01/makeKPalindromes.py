from collections import defaultdict
def canConstruct(s: str, k: int) -> bool:
    if len(s) < k: return False
    
    odds = 0
    d = defaultdict(int)
    for l in s:
        d[l] += 1
        if d[l]%2==1: odds+=1
        else: odds-=1

    if odds > k: return False
    else: return True
    
print(canConstruct("annabelle", 2))