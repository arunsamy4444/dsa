def Selection_Sort(nums):
    for i in range(len(nums)-1):
        min = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[i],nums[min] = nums[min],nums[i]
    return nums   
    
print(Selection_Sort([8,3,7,1,5,2]))