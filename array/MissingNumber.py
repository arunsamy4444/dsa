def MissingNumber(nums):   
    nums.sort()
    for i in range(0,len(nums)):
        if nums[i] != i:
            return i

    return len(nums)
        
            
print(MissingNumber([3,0,1]))