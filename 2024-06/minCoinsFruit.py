from typing import List

def minimumCoins(prices: List[int]) -> int:
        temp = [(0,0)]
        for i in range(len(prices)):
            pos,new = 2 * i + 2, temp[0][1] + prices[i]
            if i == temp[0][0]:
                temp.pop(0)
            while temp:
                print(temp)
                if temp[-1][1] >= new:
                    temp.pop()
                else:
                    break
            temp.append((pos,new))
        return temp[0][1]

print(minimumCoins(prices=[27,17,29,45,3,39,42,26]))