from typing import List

MOD = 10 ** 9 + 7
MX = 10 ** 5 + 1
p_scores = [0] * MX
for i in range(2, MX): 
    if p_scores[i] == 0: 
        for j in range(i, MX, i): 
            p_scores[j] += 1

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = [-1] * n
        right = [n] * n
        st = []
        for i, v in enumerate(nums): 
            while st and p_scores[nums[st[-1]]] < p_scores[v]: 
                right[st.pop()] = i
            if st: 
                left[i] = st[-1]
            st.append(i)

        ans = 1
        for i, v, l, r in sorted(zip(range(n), nums, left, right), key=lambda x: -x[1]): 
            tot = (i - l) * (r - i)
            if tot >= k: 
                ans = ans * pow(v, k, MOD) % MOD
                break
            ans = ans * pow(v, tot, MOD) % MOD
            k -= tot
        
        return ans

s = Solution()
print(s.maximumScore([1,7,11,1,5],14))
# print(s.maximumScore([19,12,14,6,10,18],3))