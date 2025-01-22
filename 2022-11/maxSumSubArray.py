
def maxSubArray(nums):
    size = len(nums)
    left = divide(nums[:int(size//2)])
    middle = divide(nums[int(size//2.5):int(size//1.5)])
    right = divide(nums[int(size//2):])

    return max([left,middle,right,sum(nums)])

def divide(nums):
    size = len(nums) 
    if size <= 1:
        return sum(nums)
    half = int(size//2)
    left = nums[:half]
    middle = nums[int(size//2.5):int(size//1.5)]
    right = nums[half:]

    subLeft = divide(left)
    subMiddle = divide(middle)
    subRight = divide(right)

    sumLeft = sum(left)
    sumMiddle = sum(middle)
    sumRight = sum(right)
    sumNums = sum(nums)

    return max([sumLeft,sumMiddle,sumRight,subLeft,subMiddle,subRight,sumNums])

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
