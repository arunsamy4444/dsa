def LargestNumberAtLeastTwiceofOthers(nums):
    
    larg_no = max(nums)
    larg_no_ind = nums.index(larg_no)

    for i in range(len(nums)):
        if larg_no !=nums[i] and larg_no < 2*nums[i]:
            return -1
    return larg_no_ind

    
print(LargestNumberAtLeastTwiceofOthers([3,6,1,0])) #1