from typing import List

def hash_solution(dictionary: List[str], sentence: str) -> str:
  words = sentence.split(' ')
  dictionary.sort(key=lambda s: len(s))
  d = {}
  for root in dictionary:
    l: List[str] = d.get(root[0], [])
    l.append(root)
    d[root[0]] = l
  for i,w in enumerate(words):
    if w[0] in d:
      for r in d[w[0]]:
        if w[:len(r)] == r:
          words[i] = r
          break
  return " ".join(words)

# print(hash_solution(["aa","a","b","c"], "aadsfasf absbs bbab cadsfafs"))

class TNode:
  def __init__(self) -> None:
    self.children = [None for _ in range(26)]
    self.wordCount = 0

def trie_solution(dictionary: List[str], sentence: str) -> str:
  trie = TNode()

  for key in dictionary:
    currentNode = trie
    for c in key:
      if currentNode.children[ord(c) - ord('a')] == None:
        newNode = TNode()
        currentNode.children[ord(c) - ord('a')] = newNode
      currentNode = currentNode.children[ord(c) - ord('a')]
    currentNode.wordCount += 1
      
  
  o = []
  for word in sentence.split(' '):
    currentNode = trie
    r = ''
    for i, c in enumerate(word):
      if currentNode.children[ord(c) - ord('a')] is None or i==len(word)-1:
        o.append(word)
        break
      else:
        r+=c
        if currentNode.children[ord(c) - ord('a')].wordCount > 0:
          o.append(r)
          break
        currentNode = currentNode.children[ord(c) - ord('a')]
    
  return " ".join(o)

print(trie_solution(["e","k","c","harqp","h","gsafc","vn","lqp","soy","mr","x","iitgm","sb","oo","spj","gwmly","iu","z","f","ha","vds","v","vpx","fir","t","xo","apifm","tlznm","kkv","nxyud","j","qp","omn","zoxp","mutu","i","nxth","dwuer","sadl","pv","w","mding","mubem","xsmwc","vl","farov","twfmq","ljhmr","q","bbzs","kd","kwc","a","buq","sm","yi","nypa","xwz","si","amqx","iy","eb","qvgt","twy","rf","dc","utt","mxjfu","hm","trz","lzh","lref","qbx","fmemr","gil","go","qggh","uud","trnhf","gels","dfdq","qzkx","qxw"], "qmxixtooxtbrzyorn gyvukjpc s mxhlkdaycskj uvwmerplaibeknltuvd ocnn frotscysdyclrc ckcttaceuuxzcghw pxbd oklwhcppuziixpvihihp"))