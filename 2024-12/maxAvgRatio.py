from typing import List
from heapq import heappop, heappush


def maxAverageRatio(classes: List[List[int]], extraStudents: int) -> float:
    # calc init potential ratio improvements
    ratios = []
    for i,x in enumerate(classes):
        a,b =x
        # calc new pass rate with updated students
        diff = (a/b)-((a+1)/(b+1))
        heappush(ratios, [diff,i])
    
    # take the class with the largest potential improvement
    for _ in range(extraStudents):
        # get smallest (largest)
        _,i = heappop(ratios)
        # modify class at i
        classes[i] = [classes[i][0]+1,classes[i][1]+1]
        a,b = classes[i]
        # improve it again and add it back
        npr = (a/b)-((a+1)/(b+1))
        heappush(ratios, [npr,i])
    
    return sum([a/b for a,b in classes])/len(classes)

print(maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4))
