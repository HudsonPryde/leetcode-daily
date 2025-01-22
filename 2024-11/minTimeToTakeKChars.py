from collections import Counter,deque
def takeCharacters(s: str, k: int) -> int:
    n = len(s)
    c = Counter(s)
    d = deque()
    max_len = 0
    if c['a'] < k or c['b'] < k or c['c'] < k: return -1
    for x in s:
        d.append(x)
        c[x] -= 1
        while c['a'] < k or c['b'] < k or c['c'] < k:
            c[d.popleft()] += 1
        max_len = max(max_len, len(d))
    return n-max_len


        

print(takeCharacters("aabac", 1))
