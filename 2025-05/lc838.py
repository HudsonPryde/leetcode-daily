class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        res = ''
        i,j = 0,0
        cnt = 0
        while i < n:
            if dominoes[i] == 'L':
                res += 'L'*(cnt+1)
                cnt = 0
                i += 1
            elif dominoes[i] == 'R':
                i += 1
                j = i
                res += '.'*cnt + 'R'
                cnt = 0
                while j < n:
                    if dominoes[j] == 'R':
                        res += 'R'*cnt
                        i = j
                        break
                    elif dominoes[j] == 'L':
                        r = "R"*(cnt//2)
                        l = "L"*(cnt//2) + 'L'
                        if cnt%2 == 0:
                            res += r+l
                        else:
                            res += r+'.'+l
                        i = j+1
                        break
                    elif j == n-1:
                        res += 'R'*(cnt+1)
                        i = j+1
                        break
                    else:
                        cnt += 1
                        j += 1
                cnt = 0
            else:
                cnt += 1
                i += 1
        return res + '.'*(cnt)

                
            

s = Solution()
print(s.pushDominoes("RR.L"))