def maxElement(n, maxSum, k):
    # Write your code here
    l,r = k-1, n-k
    max_k = max(l,r)+1
    t_r, t_l = 0, 0
    for i in range(l):
        t_l += max_k-1-i
    for j in range(r):
        t_r += max_k-1-j
    print(l,r,max_k,t_l,t_r)
    s = max_k + t_l + t_r
    print(s)
    max_k += max((maxSum-s)//n, 0)
    return max_k
def maxElementV2(n, maxSum, k):
    def get_sum(x, cnt):
        # Sum of 'cnt' elements starting from 'x' and decreasing by 1
        # but not going below 1
        if x > cnt:
            return cnt * (2 * x - cnt + 1) // 2  # Arithmetic progression sum
        else:
            return x * (x + 1) // 2 + (cnt - x)  # Add remaining 1's if x becomes 1

    # Binary search for the maximum value at index k
    left, right = 1, maxSum
    answer = 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Calculate the sum of the left side (0 to k-1) and right side (k+1 to n-1)
        left_sum = get_sum(mid - 1, k)
        right_sum = get_sum(mid - 1, n - k - 1)
        
        # Total sum including the element at index k
        total_sum = left_sum + mid + right_sum
        
        if total_sum <= maxSum:
            answer = mid  # Try to maximize the element at index k
            left = mid + 1
        else:
            right = mid - 1
    
    return answer
# print(maxElement(5,7,4))
print(maxElementV2(10123,1712344,4))
# k: 7
# [0,0,0,0,0]
# [0,0,0,1,0]
# [0,0,1,2,1]
# [0,1,2,3,2]
# [1,2,3,4,3]