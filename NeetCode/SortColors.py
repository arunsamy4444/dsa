def sortColors(nums):
    s = True
    while s:
        s = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
                s = True
    return nums
    
    
    
print(sortColors([1,0,1,2]))