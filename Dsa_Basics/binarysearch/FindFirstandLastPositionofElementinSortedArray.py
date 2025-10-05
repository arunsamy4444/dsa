def FindFirstandLastPositionofElementinSortedArray(nums,target):
    res=[]
    for i in range(len(nums)):
        if nums[i] == target:
            res.append(i)
    if not res:
        return [-1,-1]
    return [res[0],res[-1]]
    
    
print(FindFirstandLastPositionofElementinSortedArray([5,7,7,8,8,10],8)) # [3,4]