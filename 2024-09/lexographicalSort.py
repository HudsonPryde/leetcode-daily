from typing import List


def lexicalOrder(n: int) -> List[int]:
    l = [i for i in range(1,n+1)]
    l.sort(key=lambda x: x/10**(len(str(x))-1))
    return l
print(lexicalOrder(13))