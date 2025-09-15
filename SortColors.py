def SortColors(nums):
    for i in range(0,len(nums)-1):
        for j in range(0,len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]


    print(nums)    
    
print(SortColors([1,0,2,0,1,2]))