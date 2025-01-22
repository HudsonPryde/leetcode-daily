from typing import List


def stringMatching(words: List[str]) -> List[str]:
    seen = ""
    words.sort(key=lambda x: len(x), reverse=True)
    res = []
    for word in words:
        if word in seen:
            res.append(word)
        seen += "."+word
    return res
print(stringMatching(["mass","as","hero","superhero"]))