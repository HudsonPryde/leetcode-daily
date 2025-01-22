from typing import List
from collections import Counter

def commonChars(words: List[str]) -> List[str]:
  if len(words) == 1:
    return words[0]
  o = []
  c = set(words[0])
  for char in c:
    f = min([word.count(char) for word in words])
    o += f*[char]
  return o

print(commonChars(words=["bella","label","roller"]))