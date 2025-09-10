def remove_duplicates(nums):
    if nums == [] or len(nums) < 1:
        return 0
        
    res = []
    for i in range(len(nums)):
        Duplicate_Found = False
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                 Duplicate_Found = True
                 break
        if not Duplicate_Found:
            res.append(nums[i])
    print(res)
    return res
            
    
remove_duplicates([0,0,1,1,1,2,2,3,3,4])