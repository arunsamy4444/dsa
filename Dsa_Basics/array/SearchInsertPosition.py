def SearchInsertPosition(nums,tar):
    for i in range(len(nums)):
        if nums[i] >= tar:
            print(i)
    return len(nums)
    
    
print(SearchInsertPosition([1,3,5,6],10))