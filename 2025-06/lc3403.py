class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1: return word
        n = len(word)
        target = max(word)
        ind = [i for i,x in enumerate(word) if x == target]
        res = None
        for idx in ind:
            if idx >= numFriends-1:
                if res != None: res = max(res,word[idx:])
                else: res = word[idx:]
            else:
                if res != None: res = max(res,word[idx:n-(numFriends-idx-1)])
                else: res = word[idx:n-(numFriends-idx-1)]
        return res

s = Solution()
print(s.answerString("xzyz",3))