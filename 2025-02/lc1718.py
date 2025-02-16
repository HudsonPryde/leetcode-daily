from typing import List


def constructDistancedSequence(n: int) -> List[int]:
    res = [0 for _ in range((n*2)-1)]
    nums = [i for i in range(1,n+1)]

    def helper(nums, res, idx):
        if not nums:
            return res
        if res[idx] != 0:
            return helper(nums,res,idx+1)
        for i in range(len(nums)-1,-1,-1):
            num = nums[i]
            if num == 1:
                n_res = res[:]
                n_res[idx] = num
                n_nums = nums[:i]+nums[i+1:]
                n_res = helper(n_nums,n_res,idx+1)
                if n_res:
                    return n_res
                continue
            if idx+num >= len(res): return False
            elif res[idx+num] == 0:
                n_res = res[:]
                n_res[idx] = num
                n_res[idx+num] = num
                n_nums = nums[:i]+nums[i+1:]
                n_res = helper(n_nums,n_res,idx+1)
                if n_res:
                    return n_res
        return False
    return helper(nums,res,0)


print(constructDistancedSequence(6))
    
    

