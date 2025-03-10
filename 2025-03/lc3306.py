from collections import Counter


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self._helper(word, k) - self._helper(word, k+1)
    def _helper(self, word: str, k: int):
        vowels = set(['a','e','i','o','u'])
        n = len(word)
        v = Counter()
        c = 0
        res = 0
        left,right = 0,0
        while right < n:
            l = word[right]
            if l in vowels:
                v[l] += 1
            else:
                c += 1
            while len(v) == 5 and c >= k:
                res += n-right
                s = word[left]
                if s in vowels:
                    v[s] -= 1
                    if v[s] == 0:
                        del v[s]
                else:
                    c -= 1
                left += 1
            right += 1
        return res
        
                
        
s = Solution()
print(s.countOfSubstrings("aadieuoh",1))