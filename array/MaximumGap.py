def MaximumGap(nums):
    if len(nums) < 2:
        return 0
    nums.sort()
    max_gap = 0
    for i in range(len(nums)-1):
        current_gap = nums[i+1] - nums[i] 
        if max_gap < current_gap:
            max_gap = current_gap
    return max_gap
    
    
print(MaximumGap([3,6,9,1]))
# print(MaximumGap([10]))