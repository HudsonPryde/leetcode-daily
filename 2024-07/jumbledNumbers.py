from typing import List
import heapq


# def sortJumbled(mapping: List[int], nums: List[int]) -> List[int]:
#     heap = []
#     for num in nums:
#         m_num = ''
#         for digit in str(num):
#             m_num += str(mapping[int(digit)])
#         m_num = m_num.lstrip('0')
#         if not m_num:
#             m_num = '0'
#         heap.append((int(m_num), num))
#     heap.sort(key=lambda x: x[0])
#     return [x[1] for x in heap]

def sortJumbled(mapping: List[int], nums: List[int]) -> List[int]:
    t_rule = str.maketrans({str(i):str(x) for i,x in enumerate(mapping)})
    return sorted(nums, key=lambda x: int(str(x).translate(t_rule)))

print(sortJumbled([8,9,4,0,2,1,3,5,7,6], [991,338,38]))