def SortanArray(nums):
    swapped = True
    while swapped:
        swapped = False
        l=0
        while l < len(nums)-1:
            r=l+1
            if nums[l] > nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                swapped = True
            l+=1
    return nums
            

    
    
    
print(SortanArray([5,1,1,2,0,0]))