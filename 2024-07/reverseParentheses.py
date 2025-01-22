from collections import deque


def reservePara(s: str) -> str:
  s = list(s)
  d = []
  for i, l in enumerate(s):
      if l == "(":
          d.append(i)
      elif l == ")":
          p = d.pop()
          s[p:i] = reversed(s[p:i])
  return "".join(m for m in s if m not in "()")

# print(reservePara("(abcd)"), " expect: dcba")
# print(reservePara("(u(love)i)"), " expect: iloveu")
print(reservePara("(abc(def(ghi(jkl)mno)pqr)stu(vwx)yz)"), " expect: zyvwxutsdefonmjklihgpqrcba")