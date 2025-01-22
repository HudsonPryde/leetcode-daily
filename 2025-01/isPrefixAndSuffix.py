from typing import List


def countPrefixSuffixPairs(words: List[str]) -> int:
    n = len(words)
    res = 0
    for i in range(n):
        word = words[i]
        for j in range(i, n):
            if j == i or len(words[j]) > len(word): continue
            if word.startswith(words[j]) and word.endswith(words[j]): res += 1
    return res
