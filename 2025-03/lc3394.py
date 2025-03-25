from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        v_rects = sorted(rectangles,key=lambda x: [x[1],x[3]])
        h_rects = sorted(rectangles,key=lambda x: [x[0],x[2]])
        cuts = 0
        prev = None
        temp1 = []
        temp2 = []
        for l,b,r,t in v_rects:
            if prev == None:
                prev = (l,b,r,t)
                continue
            pl,pb,pr,pt = prev
            if b >= pt:
                cuts += 1
                temp1.append([prev,(l,b,r,t)])
            # if cuts == 2: return True
            prev = (max(l,pl),max(b,pb),max(r,pr),max(t,pt))
        cuts = 0
        prev = None
        for l,b,r,t in h_rects:
            if prev == None:
                prev = (l,b,r,t)
                continue
            pl,pb,pr,pt = prev
            if l >= pr:
                cuts += 1
                temp2.append([prev,(l,b,r,t)])
            # if cuts == 2: return True
            prev = (max(l,pl),max(b,pb),max(r,pr),max(t,pt))
        # return False
        return cuts,temp1,temp2
    
s = Solution()
print(s.checkValidCuts(3,[[0,0,1,3],[1,0,2,2],[2,0,3,2],[1,2,3,3]]))