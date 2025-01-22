def merge(nums1, m, nums2, n):
    if m == 0:
        nums1[:] = nums2[:]
    else:
        nums1 = nums1[:m]
        i = 0
        while len(nums2) > 0:
            if i >= len(nums1):
                num2 = nums2.pop(0)
                nums1.append(num2)
            elif nums2[0] <= nums1[i]:
                num2 = nums2.pop(0)
                nums1.insert(i, num2)
            i += 1
    return nums1
print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
