from typing import List

def numTeams(rating: List[int]) -> int:
    total = 0
    for i in range(1, len(rating)-1):
        rat = rating[i]
        smaller_l, smaller_r = 0,0
        larger_l, larger_r = 0,0
        for j in range(len(rating)):
            if j < i:
                if rating[j] < rat:
                    smaller_l += 1
                else:
                    larger_l += 1
            elif j > i:
                if rating[j] > rat:
                    larger_r += 1
                else:
                    smaller_r += 1
        total += (smaller_l*larger_r) + (smaller_r*larger_l)
    return total

print(numTeams([2,5,3,4,1]))