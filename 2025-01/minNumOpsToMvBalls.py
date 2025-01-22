from typing import List


def minOperations(boxes: str) -> List[int]:
    n = len(boxes)
    r_boxes = 0
    r_sum = 0
    for i in range(n):
        if boxes[i] == "1":
            r_sum += i
            r_boxes += 1
    l_sum = 0
    l_boxes = 0
    res = []
    for i in range(n):
        # calc right sum distance
        r_dist = r_sum-(i*r_boxes)
        # calc left sum distance
        l_dist = (i*l_boxes)-l_sum
        res.append(r_dist+l_dist)
        # update sums
        if boxes[i] == "1":
            l_sum += i
            r_sum -= i
            r_boxes -= 1
            l_boxes += 1
    return res
print(minOperations("001011"))