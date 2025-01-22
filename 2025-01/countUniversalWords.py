from typing import List
from collections import defaultdict

def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    res = set(words1)
    letters = defaultdict(int)
    for w in words2:
        for l in w:
            letters[l] = max(letters[l], w.count(l))
    for w in words1:
        for l in letters:
            if w.count(l) < letters[l]:
                res.remove(w)
                break
    return list(res)

print(wordSubsets(["acaac","cccbb","aacbb","caacc","bcbbb"], ["caccacacac","ccaabbab","b"]))