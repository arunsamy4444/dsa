def maxSubArray(nums):
    max_sum = nums[0]
    current = 0
    for i in nums:
        if current < 0:
            current = 0
        current +=i
        if current > max_sum:
            max_sum = current
    return max_sum

        
    
# Test example
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))