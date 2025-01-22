class TNode():
    def __init__(self, value):
        self.children = [None for _ in range(10)]
        self.value = value
        

def findKthNumber(n: int, k: int) -> int:
    l = len(str(n))
    root = TNode(1)
    root.children.pop(0)
    def helper(root, d):
        if d == l:
            return
        for i in range(len(root.children)):
            node = TNode(i)
            root.children[i] = node
            helper(node, d+1)
    helper(root, 0)
    def find(root, i, lex):
        if root.children[0] == None:
            return
        for c in root.children:
            i+=1
            if i == k:
                return lex+str(c.value)
            p = find(c, i, lex+str(c.value))
            if p:
                return p
            
    return find(root, 1, str(root.value))

# [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
def helper(a,b,n):
    gap = 0
    while a <= n:
        gap += min(n+1,b)-a
        a *= 10
        b *= 10
    return gap
def findKthNumberV2(n: int, k: int) -> int:
    num = 1
    i = 1
    while i < k:
        req = helper(num, num+1, n)
        if i + req <= k:
            i += req
            num += 1
        else:
            i += 1
            num *= 10
    return num
print(findKthNumberV2(13, 2))