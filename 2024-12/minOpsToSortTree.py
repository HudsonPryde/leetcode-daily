
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def minimumOperations(root: Optional[TreeNode]) -> int:
    res = 0
    q = deque([(root, 0)])
    d = {}
    while q:
        node, depth = q.popleft()
        if depth not in d:
            res += helper(d[depth-1])
            d[depth] = [node.val]
        else:
            d[depth].append(node.val)
        if node.left:
            q.append((node.left, depth+1))
        if node.right:
            q.append((node.right, depth+1))
    
    def helper(nums: list):
        res = 0
        s = sorted(nums)
        ind = {v:i for i,v in enumerate(nums)}
        for j in range(len(nums)):
            if nums[j] != s[j]:
                idx = ind[s[j]]
                nums[j], nums[idx] = nums[idx], nums[j]
                res += 1
        return res


    return res


def helper(nums: list):
    res = 0
    d = {v:i for i,v in enumerate(nums)}
    s = sorted(nums)
    for i in range(len(nums)):
        if nums[i] != s[i]:
            idx = d[s[i]]
            d[nums[i]], d[s[i]] = d[s[i]], d[nums[i]]
            nums[i], nums[idx] = nums[idx], nums[i]
            res += 1
    return res
            


print(helper([7,6,8,5]))