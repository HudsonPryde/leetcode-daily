from typing import List
import math

class Node:
    def __init__(self, val, length=1, prev=None):
        self.val = val
        self.length = length
        self.prev = prev
def longestSquareStreak(nums: List[int]) -> int:
    m = {}
    nums.sort()
    longest_streak = -1
    for n in nums:
        k = math.sqrt(n)
        if k in m:
            m[n] = Node(n, m[k].length+1, m[k])
            if m[n].length > longest_streak:
                longest_streak = m[n].length
        else:
            m[n] = Node(n)
    
    return longest_streak

def longestSquareStreakV2(nums: List[int]) -> int:
    m = set(nums)
    nums = sorted(m)
    max_streak = -1
    for n in nums:
        streak = 0
        curr = n
        while curr in m:
            streak += 1
            m.remove(curr)
            curr = curr**2
        if streak > 1:
            max_streak = max(streak, max_streak)
    
    return max_streak

print(longestSquareStreakV2([2,3,5,6,7]))
            

